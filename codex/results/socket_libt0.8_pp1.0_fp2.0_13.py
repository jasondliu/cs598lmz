import socket
import select
import util
import threading

def server_init(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((host, port))
	s.listen(5)
	s.setblocking(False)
	return s

class Connection:
	def __init__(self, sock):
		self.sock = sock
		self.buffer = ''

	def close(self):
		self.sock.close()

	def write(self, data):
		self.sock.sendall(data)

	def read(self, n):
		try:
			while len(self.buffer) < n:
				data = self.sock.recv(4096)
				if len(data) == 0:
					raise IOError('client disappeared')
				self.
