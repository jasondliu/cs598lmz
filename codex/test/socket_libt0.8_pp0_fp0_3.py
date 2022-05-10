import socket

s = socket.socket()

host = socket.gethostname()
port = 12397
s.connect((host, port))
