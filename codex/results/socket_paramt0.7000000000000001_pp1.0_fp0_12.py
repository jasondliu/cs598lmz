import socket
socket.if_indextoname(3)

#socket.socket(family=AF_INET, type=SOCK_DGRAM, proto=0, fileno=None)
#from socket import *
#socket(AF_INET, SOCK_DGRAM, 0)

from socket import *
s = socket(AF_INET, SOCK_DGRAM)
s.connect(('www.python.org', 80))
s.send(b'GET /index.html HTTP/1.0\r\n\r\n')
print(s.recvfrom(4096))

#from socket import socket, AF_INET, SOCK_DGRAM
#s = socket(AF_INET, SOCK_DGRAM)
#s.sendto(b'', ('www.python.org', 80))
#print(s.recvfrom(4096))

#from socket import *
#s = socket(AF_INET, SOCK_STREAM)
#s.bind(('', 8000))
#s.listen(5)
#s.accept()

#from
