import select
import socket
import sys
import time
import threading
import Queue
import json
import os

class Server(object):
	def __init__(self, port, host='', backlog=5):
		self.clients = 0
		self.clientmap = {}
		self.outputs = []
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.server.bind((host, port))
		print 'Server listening to port', port
		self.server.listen(backlog)
		self.server.setblocking(0)
		self.inputs = [self.server, sys.stdin]
		self.running = 1
		self.queue = Queue.Queue()
		self.thread = threading.Thread(target=self.handle_data)
		self.thread.start()

	def handle_data(
