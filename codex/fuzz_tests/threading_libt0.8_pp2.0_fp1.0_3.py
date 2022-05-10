import threading
threading.stack_size(1024000)

ESTADO_LISTENER = 0
ESTADO_RESPONDER = 1

class MiTcpHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		self.data = self.request.recv(1024).strip()
		print "{} wrote:".format(self.client_address[0])
		print self.data
		# just send back the same data, but upper-cased
		self.request.sendall(self.data.upper())

class Listener(threading.Thread):
	def __init__(self, host, port):
		threading.Thread.__init__(self)
		self.host = host
		self.port = port

	def run(self):
		global lock
		global ESTADO_LISTENER
		global ESTADO_RESPONDER
		global server

		server = TCPServer((self.host, self.port), MiTcpHandler)
		while True:
			lock
