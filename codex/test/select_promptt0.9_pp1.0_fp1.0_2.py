import select
# Test select.select function
import socket
from time import sleep

if __name__ == '__main__':
	server = socket.socket()
	server.bind(('127.0.0.1', 5000))
	server.listen()
	conn,addr = server.accept()
	conn.setblocking(False)
	while True:
		sleep(2)
		try:
			print(conn.recv(1024).decode())
		except  Exception as e:
			txt = 'pangbai'
			print('数据库更新')
