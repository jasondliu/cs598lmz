import select
# Test select.select()

import select
import socket

s = socket.socket()
s.bind(('localhost', 50000))
s.listen(1)

conn, addr = s.accept()
print('Connected by', addr)

while True:
    data = conn.recv(1024)
    if not data: break
    conn.send(data)

conn.close()

# Test select.poll()

import select
import socket

s = socket.socket()
s.bind(('localhost', 50000))
s.listen(1)

conn, addr = s.accept()
print('Connected by', addr)

while True:
    data = conn.recv(1024)
    if not data: break
    conn.send(data)

conn.close()

# Test select.epoll()

import select
import socket

s = socket.socket()
s.bind(('localhost', 50000))
s.listen(1)

conn, addr = s.accept()
print('Connected by', addr)

while True
