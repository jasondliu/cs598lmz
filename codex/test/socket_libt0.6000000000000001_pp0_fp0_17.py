import socket
import threading
import os

class Client:
	def __init__(self, ip, port):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((ip, port))

		msg_recv = threading.Thread(target=self.msg_recv)

		msg_recv.daemon = True
		msg_recv.start()

		while True:
			msg = input()
			if msg == 'quit':
				self.sock.send(str.encode(msg))
				self.sock.close()
				os._exit(0)
			else:
				self.sock.send(str.encode(msg))

