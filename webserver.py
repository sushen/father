
from http.server import BaseHTTPRequestHandler, HTTPServer

class webserverHandler (BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith('/hello'):
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()

                output =b""
                output += b"<html>"
                output += b"<h1>Hello</h1>"
                output += b"</html>"
                self.wfile.write(output)
                #self.wfile.write(output)#"<body><h1>This is a test.</h1></body>")
                print(output)
                return

        except IOError:
            self.send_error(404, "file not found %s" % self.path)

def main():
    try:
        port = 8000
        server = HTTPServer(('',port), webserverHandler)
        print("web server poet %s" %port)
        server.serve_forever()


    except KeyboardInterrupt:
        print("^C Entered , Stopping server")
        server.socket.close()

if __name__ == '__main__':
    main()