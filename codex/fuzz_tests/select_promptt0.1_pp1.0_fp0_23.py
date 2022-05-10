import select
# Test select.select()

import socket

s = socket.socket()
s.bind(('localhost', 50000))
s.listen(1)

conn, addr = s.accept()
print('Connected by', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
conn.close()
