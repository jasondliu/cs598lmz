import socket

s = socket.socket()
host = socket.gethostname()
port = 1234

s.connect((host,port))
