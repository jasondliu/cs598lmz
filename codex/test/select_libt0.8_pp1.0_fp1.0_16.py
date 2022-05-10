import select

import sys

def getData():
	data = ""
	try:
		while True:
			inputready, outputready, exceptready = select.select([sys.stdin], [], [])
			if inputready:
				data += sys.stdin.read(1)
	except:
		return data

class Gumball:
	def __init__(self, port):
		self.conn = socket.create_connection(('localhost', port))
		self.data = ""

	def send(self, msg):
		msg += "\n"
		self.conn.send(msg)
	
	def recv(self, prompt = False):
		data = ""
		while True:
			inputready, outputready, exceptready = select.select([self.conn], [], [])
			if inputready:
				data += self.conn.recv(1)
			if data.endswith("\n"):
				break
