import selectors
import traceback

sel = selectors.DefaultSelector()

class chatServer(object):

	def __init__(self, ip, port):
		self.ip = ip
		self.port = port
		self.lsock = socket.socket()

	def bind(self):
		try:
			self.lsock.bind((self.ip, self.port))

			self.lsock.listen(10)
			print("listening...")
			self.lsock.setblocking(False)

			sel.register(self.lsock, selectors.EVENT_READ, self.accept_connection)
		except Exception as e:
			print(e)
			sys.exit(0)

