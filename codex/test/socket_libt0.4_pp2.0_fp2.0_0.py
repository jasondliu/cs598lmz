import socket
import sys
import time
import threading
import os

class Client:
	def __init__(self,host,port,file_name):
		self.host = host
		self.port = port
		self.file_name = file_name
		self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.socket.connect((self.host,self.port))

	def send_file(self):
		file = open(self.file_name,'rb')
		file_size = os.path.getsize(self.file_name)
		self.socket.send(bytes(str(file_size),'utf-8'))
		time.sleep(0.1)
		while True:
			data = file.read(1024)
			if not data:
				break
			self.socket.send(data)
			time.sleep(0.1)
		file.close()
		self.socket.close
