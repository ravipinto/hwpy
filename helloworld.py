""" This application implements a plain Hello World webserver """
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class TestHttpServerRequestHandler(BaseHTTPRequestHandler):
    """ Main class of our app """

    def do_GET(self):
        """ HTTP GET method implementation """
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

def run():
    """ Main execution block """
    # print('starting server...')

    accs_hostname = os.getenv('HOSTNAME')
    print('HOSTNAME = ' + accs_hostname)
    # if accs_hostname is None:
    #     accs_hostname = 'localhost'
    # print('HOSTNAME = ' + accs_hostname)
    accs_port = os.getenv('PORT')
    print('PORT = ' + str(accs_port))
    if accs_port is None:
        accs_port = 9000
    else:
        accs_port = int(accs_port)
    print('PORT = ' + str(accs_port))
    server_address = (accs_hostname, accs_port)
    httpd = HTTPServer(server_address, TestHttpServerRequestHandler)
    # print('running server...')
    httpd.serve_forever()

run()
