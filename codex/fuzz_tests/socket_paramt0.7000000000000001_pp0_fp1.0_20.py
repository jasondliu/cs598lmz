import socket
socket.if_indextoname(2)

'lo0'

socket.if_nametoindex('en1')

7

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 2525))
s.connect(('www.python.org', 80))
s.sendall('GET / HTTP/1.0\r\n\r\n')
data = s.recv(1024)
print 'Received', repr(data)
s.close()

'Received \'HTTP/1.1 301 Moved Permanently\\r\\nServer: nginx\\r\\nDate: ......\''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 2525))
s.connect(('www.python.org', 80))
s.sendall('GET / HTTP/1.0\r\n\r\n')
s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('
