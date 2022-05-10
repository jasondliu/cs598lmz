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

