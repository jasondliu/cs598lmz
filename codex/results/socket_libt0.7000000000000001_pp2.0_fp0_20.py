import socket
import time
import threading
from datetime import datetime
from collections import deque

class TCPServer():

	def __init__(self, host='127.0.0.1', port = 65432):
		self.host = host
		self.port = port
		self.is_listening = False
		# self.buffer_size = buffer_size
		self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_socket.bind((host, port))
		self.server_socket.listen()
		self.client_sockets = []
		self.connected_clients = []
		self.client_file_descriptors = []
		self.client_addresses = []
		self.client_messages = []
		self.message_queue = deque()
		self.buffer_size = 1024

	def __del__(self):
		if self.is_listening:
			self.stop_
