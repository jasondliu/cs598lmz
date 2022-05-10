import socket
import time
threading._DummyThread._Thread__stop = lambda x: 42
import readline

class TCP():
	''' An implementation of a threaded TCP server '''

	def __init__(self, host, port, source_addr=''):

		self.keep_running = False
		self.client_threads = []
		self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
