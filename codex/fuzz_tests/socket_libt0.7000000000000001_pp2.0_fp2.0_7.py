import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 0))
s.listen(1)

print(s.getsockname()[1])
conn, addr = s.accept()

while True:
    data = conn.recv(1024)
    if not data: break

    conn.send(data)

conn.close()
