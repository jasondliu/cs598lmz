import socket

s = socket.socket()
port = 12345
s.bind(('', port))
s.listen(5)
