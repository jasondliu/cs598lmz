import _struct

# socket
import socket
import io
import _socket

# select
import select

# json
import json

# debug
import debug
import debug_server

# buff ered string
import buffered_string

# http connection
import http_connection

# constants
import constants

# threading
import _thread

# util
import util

# Server
class Server:
	
	# HTTP Server
	def __init__(self, port, callback, debug_name=None):
		# set debug mode
		debug.DEBUG_MODE = True
		# create a new debug server
		self.debug_server = debug_server.DebugServer()
		# port
		self.port = port
		# request callback
		self.callback = callback
		# debug name
		if debug_name is None:
			self.debug_name = "server"
		else:
			self.debug_name = debug_name
		# Server frame
