import select, socket, sys
import threading

class Server(object):
	"""
	"""
	def __init__(self):
		self.host = ''
		self.port = 5150
		self.backlog = 5
		self.size = 1024
		self.server = None
		self.threads = []

