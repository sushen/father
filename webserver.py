
from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data_map import Base, UserInfo, UserAddress
engine = create_engine('sqlite:///father.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
session.query(UserInfo).all()
session.query(UserAddress).all()

class webserverHandler (BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html>"
                output += "<h1>Welcome</h1>"
                output += "<a href='/user'>Go to All Users</a>"
                output += "</br>"
                output += "</body></html>"
                self.wfile.write(bytes(output, 'utf-8'))
                return

            if self.path.endswith('/user'):
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h1> All Our Registerd User</h1>"
                output += "</br>"
                output += "<h3> <a href ='/user/new'> Add New User</a></h3>"

                output += "</br>"


                users = session.query(UserInfo).all()
                for user in users:
                    output += str(user.id)
                    output += "</br>"
                    output += str(user.email)
                    output += "<br/>"
                    output += "<a href = '/user/edit'> Edit </a>"
                    output += "<br/>"
                    output += "<a href = '/user/delete'> Delete </a>"
                    output += "</br></br>"


                output += "</body></html>"

                self.wfile.write(bytes(output, 'utf-8'))
                print(output)
                return

            if self.path.endswith('/user/new'):
                users = session.query(UserInfo).all()
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"

                output += "<h2>New User form</h1>"
                output += "<h4><a href = '/user'> See all User </a></h4>"

                output += '''<form method='POST' enctype='multipart/form-data' action='/user/new'><h2>Enter the user email address</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''

                output += "</body></html>"
                self.wfile.write(bytes(output, 'utf-8'))
                print(output)
                return

            if self.path.endswith('/user/edit'):
                users = session.query(UserInfo).all()
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"

                output += "<h2>Edit User </h1>"

                output += "</body></html>"
                self.wfile.write(bytes(output, 'utf-8'))
                print(output)
                return

            if self.path.endswith('/user/delete'):
                users = session.query(UserInfo).all()
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"

                output += "<h2>Delete User </h1>"

                output += "</body></html>"
                self.wfile.write(bytes(output, 'utf-8'))
                print(output)
                return


        except IOError:
            self.send_error(404, "file not found %s" % self.path)


    def do_POST(self):
        try:
            if self.path.endswith("/user/new"):
                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
                pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('message')

                output = ""
                output += "<html><body>"
                output += "<h4><a href = '/user'> See all User </a></h4>"

                output += " <h2> You Add a new user and the mail address is: </h2>"

                newUser = UserInfo(email=messagecontent[0])
                session.add(newUser)
                session.commit()

                output += "<h1> %s </h1>" % messagecontent[0]

                output += '''<form method='POST' enctype='multipart/form-data' action='/user/new'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''

                output += "</body></html>"

                self.wfile.write(bytes(output, 'utf-8'))
                #print (output)
                return

        except:
            pass

def main():
    try:
        port = 8000
        server = HTTPServer(('',port), webserverHandler)
        print("web server uri http://localhost:%s" %port)
        server.serve_forever()


    except KeyboardInterrupt:
        print("^C Entered , Stopping server")
        server.socket.close()

if __name__ == '__main__':
    main()
