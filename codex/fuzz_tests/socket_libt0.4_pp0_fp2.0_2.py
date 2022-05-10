import socket

#TODO: make a class for this, so that we can have multiple instances

class Client(object):
	"""
	This is a class that represents a client.
	"""

	def __init__(self, name, host, port, password):
		self.name = name
		self.host = host
		self.port = port
		self.password = password
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect((self.host, self.port))
		self.socket.send(self.password)
		self.socket.send(self.name)
		self.socket.send(self.name)

	def send(self, message):
		self.socket.send(message)

	def close(self):
		self.socket.close()

class Server(object):
	"""
	This is a class that represents a server.
	"""

	def __init__(self, name, host, port, password, clients):

