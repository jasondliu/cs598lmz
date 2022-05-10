import select
import time
import errno
import sys
import signal
# Python 2/3 compatibility.
if sys.version_info > (3,):
	unicode = str
	long = int


class SubEthaError(Exception):
	"""
	Base class for exceptions raised by this module.
	"""
	pass


class ConnectionClosed(SubEthaError):
	"""
	Connection has been closed unexpectedly.
	"""
	pass


class MessageTooLong(SubEthaError):
	"""
	Message can't be sent because it's longer than allowed.
	"""
	pass


class WrongEndianness(SubEthaError):
	"""
	Message from client uses different endianness than set in options.
	"""
	pass




class Client(object):
	"""Handler for low-level communication with a single client."""
	def __init__(self, socket, endianness, opts):
		self.socket = socket
		self.addr = socket.getpeername()
		self.endianness = endianness
		self.op
