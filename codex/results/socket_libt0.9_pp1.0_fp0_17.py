import socket
import time
from threading import Timer
import struct

server_addr = ('localhost', 10000)

def send_msg():
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(server_addr)
	if __name__ == '__main__':
		main(client)

def main(client):
	# 计数器
	count = 0

	while 1:
		count = count + 1

		print "count value:", count
		l = client.send(str(count))
		msg = client.recv(1024)  # 收到的数据
		print msg
		time.sleep(8)
		client.close()
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			client.connect(server_addr)
		except Exception:
			print "Reconnect!"
			client.connect(server_
