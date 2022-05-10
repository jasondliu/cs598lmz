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
