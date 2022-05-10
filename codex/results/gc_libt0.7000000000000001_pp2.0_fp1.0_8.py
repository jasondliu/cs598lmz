import gc, weakref
import socket
import logging
import traceback

log = logging.getLogger('freenet')

def default_disconnect(self):
	try:
		self.close()
	except:
		pass

class BaseProtocol(asyncore.dispatcher):
	"""
		This is the base class of all networking protocol.
		It handles connection, disconnection, etc.

		It will never be instantiated directly.
	"""
	def __init__(self, sock=None, map=None):
		# Protocols use this as an acronym for the name of the protocol
		self.proto = 'BASE'
		# Protocols use this to keep track of what peer they are talking to
		self.peer_id = 'UNKNOWN'
		# Protocols will use this to store a reference to what entity the
		# peer belongs to
		self.entity = None

		# Protocols will use this to store the data that has been received
		# but not yet processed by the protocol
		self.data = ''
