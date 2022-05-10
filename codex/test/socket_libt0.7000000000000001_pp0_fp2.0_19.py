import socket
import threading

from core.logger import Logger

class ChatClient:
	"""
	Class to represent a Chat Client
	"""
	def __init__(self, host, port, name=''):
		"""
		Creates a ChatClient and starts a thread to listen to messages.
		
		Parameters:
			host (String): Host the ChatServer is hosted on.
			port (int): Port ChatServer is hosted on.
			name (String): Name of ChatClient.
		"""
		self.host = host
		self.port = port
		self.name = name
		self.logger = Logger(self.name)
		
		# Create connection to server
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((self.host, self.port))
		
		# Start thread to listen for messages
