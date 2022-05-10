import select
# Test select.select() with a timeout

import socket
import select
import sys

host = ''
port = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

while 1:
    conn, addr = s.accept()
