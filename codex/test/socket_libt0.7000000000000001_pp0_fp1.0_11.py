import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 9999

s.connect((host, port))

while 1:
    data = s.recv(1024)
    if not data: break
