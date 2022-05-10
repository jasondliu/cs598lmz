import socket
socket.if_indextoname(2)

# Using the socket API in python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.python.org', 80))
s.sendall(b'GET / HTTP/1.0\r\nHost: www.python.org\r\n\r\n')
data = s.recv(1024)
print(data)
s.close()

# Sending and receiving UDP datagrams
import socket, sys
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MAX = 65535
PORT = 1060
if sys.argv[1:] == ['server']:
    s.bind(('127.0.0.1', PORT))
    print('Listening at', s.getsockname())
    while True:
        data, address = s.recvfrom(MAX)
        print('The client at', address, 'says', repr(data))
