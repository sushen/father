
from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

class webserverHandler (BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith('/hello'):
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()

                output = b""
                output += b"<html>"
                output += b"<h1>Welcome</h1>"
                output += b"<a href="
                output += b"/"
                output += b">Go to WELCOME</a>"
                # output += b"<html>"
                # output += b"<h1>Hello</h1>"
                output += b"</html>"
                output += b"<html><body>"
                output += b"<h1>HELLO</h1>"
                output += b'''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += b"</body></html>"
                self.wfile.write(output)
                #self.wfile.write(output)#"<body><h1>This is a test.</h1></body>")
                print(output)
                return

            if self.path.endswith('/'):
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()

                output =b""
                output += b"<html>"
                output += b"<h1>Welcome</h1>"
                output += b"<a href="
                output += b"/hello"
                output += b">Go to Hello</a>"
                # output += b"</html>"
                # output += b""
                # output += b"<html><body>"
                output += b"<h1>&#161 Hola !</h1>"
                output += b'''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += b"</body></html>"
                self.wfile.write(output)
                print(output)
                return


        except IOError:
            self.send_error(404, "file not found %s" % self.path)


    def do_POST(self):
        try:
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            ctype, pdict = cgi.parse_header(
                self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')
            output = b""
            output += b"<html><body>"
            output += b" <h2> Okay, how about this: </h2>"
            output += b"<h1> %s </h1>" % messagecontent[0]
            output += b'''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            output += b"</body></html>"
            self.wfile.write(output)
            print (output)
        except:
            pass

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
