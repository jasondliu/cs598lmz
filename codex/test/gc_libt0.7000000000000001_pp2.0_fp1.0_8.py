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

