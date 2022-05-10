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
		self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		try:
			self.server_socket.bind((host, port))
		except:
			print 'Failed to bind to %s:%s' % (host, port)
			sys.exit(1)
		
		if host.strip() == '':
			host = 'localhost'
		self.host = host
		self.port = port
		self.source_addr = source_addr
		
