import socket
import time
import sys

s = socket.socket()

host = socket.gethostname()
port = 1098
s.bind((host, port))

s.listen(5)

while True:
	x = 0
	conn, addr = s.accept()
	print("Connection established with ", addr)
	while(x < 10):
		data = conn.recv(1024)
		data = data.decode()
		print(data)
		time.sleep(1)
		x +=1
	conn.close()
