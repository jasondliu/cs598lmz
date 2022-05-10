import socket
import time
import sys

host = ''
port = 50000
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)

client, address = s.accept()
while 1:
    data = client.recv(size)
    print data
    if data:
        client.send(data)

client.close()
