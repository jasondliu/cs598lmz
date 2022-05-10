import socket
socket.if_indextoname(1)
'lo0'
socket.if_indextoname(3)
'en0'
socket.if_indextoname(4)
'en1'

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.python.org',80))
s.getsockname()
('192.168.1.6', 55247)
s.getpeername()
('151.101.245.223', 80)

s.sendall(b'GET /index.html HTTP/1.0\r\n\r\n')
data = s.recv(1000)
print(data)
