import socket
import thread
import time

class Client:

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def sendMsg(self):
		while True:
			self.s.send(raw_input())
		
		

	def __init__(self, address):
		self.s.connect(address)

		thread.start_new_thread(self.sendMsg, ())

		while True:
			data = self.s.recv(1024)
			if not data:
				break
