import select
import socket
import ssl
import sys
import time

def send_request(s):
    s.send("GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n")

def receive_response(s):
    response = bytearray()
    while True:
        r, w, x = select.select([s], [], [])
        if s not in r:
            continue
        buf = s.recv(4096)
        if not buf:
            break
        response.extend(buf)
    return response

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ssl = ssl.wrap_socket(server)
server_ssl.connect(("www.google.com", 443))

