import socket
socket.if_indextoname(2)

# 3.2
from socket import *
try:
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(("", 15000))
    s.listen(5)
    c, a = s.accept()
    data = c.recv(1024)
    print('Received: ', repr(data))
finally:
    s.close()

# 3.3
from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(("www.python.org", 80))
s.sendall(b"GET / HTTP/1.0\n\n")
print(s.recv(1000))

# 3.4
from socket import *
try:
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("www.python.org", 80))
    s.sendall(b"GET / HTTP/1.0\n\n")
    print(s.recv(1000))
finally:
    s.close
