import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8001))

print('the local time is %s' % s.recv(1024))

s.close()
