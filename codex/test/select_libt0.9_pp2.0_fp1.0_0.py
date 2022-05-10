import select
from Modules.Server.csrefactored.base.client import SimpleClient

#Protocol
class SignInProtocol:
	
	def __init__(self, connection):
		self._connection = connection
		self._buffer = ""
	
	
	def receive(self, args = None):
		# Get the data from the socket
		while "\n" not in self._buffer:
			# Wait for data to arrive, or timeout
			r, _, _ = select.select([self._connection], [], [], 60)
			if not r: return None
			
			# Grab from the socket
			data = self._connection.recv(4096)
			if not data: return None
			self._buffer += data
	
		# Separate the complete data from the buffer
		command, _, self._buffer = self._buffer.partition("\n")
		
		return command
	
