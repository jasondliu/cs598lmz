import threading
threading.stack_size(1024000)

ESTADO_LISTENER = 0
ESTADO_RESPONDER = 1

class MiTcpHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		self.data = self.request.recv(1024).strip()
