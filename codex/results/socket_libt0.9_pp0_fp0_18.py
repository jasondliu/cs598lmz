import socket
from sys import argv

MASTER = 'faust.ee.washington.edu'
PORT = 8000

class Looker(object):
	def __init__(self, master = MASTER, port = PORT):
		self.master = master
		self.port = port
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	def active_resolver_slaves(self):
		self.socket.connect((self.master, self.port))
		self.socket.send('slavecount')
		return self.socket.recv(2)
	
	def active_resolver_data_collectors(self):
		self.socket.connect((self.master, self.port))
		self.socket.send('collectorcount')
		return self.socket.recv(2)

	def active_resolver_commandos(self):
		self.socket.connect((self.master, self.port))
		self.socket.send('commandocount')
