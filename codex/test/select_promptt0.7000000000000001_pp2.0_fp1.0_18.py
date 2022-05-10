import select
# Test select.select

import select
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 20000))
s.listen(1)

while True:
    conn, addr = s.accept()
