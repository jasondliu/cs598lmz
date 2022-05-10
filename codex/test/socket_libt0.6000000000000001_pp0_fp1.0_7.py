import socket
import time

class Client:
	def __init__(self, port, host):
		self.port = port
		self.host = host
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect((self.host, self.port))

	def get(self, key):
		self.socket.send('get {}'.format(key).encode())
		value = self.socket.recv(1024).decode()
		return value

	def set(self, key, value):
		self.socket.send('set {} {}'.format(key, value).encode())
		return self.socket.recv(1024).decode()

	def delete(self, key):
		self.socket.send('delete {}'.format(key).encode())
		return self.socket.recv(1024).decode()

def main():
	c = Client(12345, '127.0.0.1')
