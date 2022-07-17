import http.server
import socketserver
from http import HTTPStatus
import os


SERVER_PORT = os.getenv("PORT")


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        print(f"Client: {self.client_address}")
        self.wfile.write(b'Hello world')


httpd = socketserver.TCPServer(('', int(SERVER_PORT)), Handler)
httpd.serve_forever()