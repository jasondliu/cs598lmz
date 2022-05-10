import socket
import threading
import time
import sys

class Client:
	def __init__(self):
		self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client_socket.connect((socket.gethostname(), 1234))

	def recv_msg(self):
		while True:
			try:
				data = self.client_socket.recv(1024).decode()
				if data:
					print(data)
			except:
				pass

	def send_msg(self, msg):
		self.client_socket.send(msg.encode())

	def start(self):
		thread_recv = threading.Thread(target=self.recv_msg, args=())
		thread_recv.start()

		while True:
			msg = input()
			self.client_socket.send(msg.encode())
			if msg == 'exit':
