import http.server
import socketserver
from http import HTTPStatus
import os
import mysql.connector
from datetime import datetime


SERVER_PORT = os.getenv("PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWD = os.getenv("DB_PASSWD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "default")


cnx = mysql.connector.connect(user=DB_USER, password=DB_PASSWD,
                              host=DB_HOST,
                              database=DB_NAME)
cnx.autocommit = True


def log_new_connection(client_address):
    cur = cnx.cursor()
    params = (datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), str(client_address))
    cur.execute(
        "INSERT INTO client_activity (date, address) VALUES (%s, %s)",
        params
    )


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        log_new_connection(self.client_address)
        self.wfile.write(b'Hello world\n')


if __name__ == '__main__':
    httpd = socketserver.TCPServer(('', int(SERVER_PORT)), Handler)
    httpd.serve_forever()
