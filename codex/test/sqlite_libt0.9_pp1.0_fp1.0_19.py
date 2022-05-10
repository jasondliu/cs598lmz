import ctypes
import ctypes.util
import threading
import sqlite3
import subprocess

# user defined modules
import screeninfo

class data_func(object):

	def __init__(self):

		self.connection_status = 0
		self.mode_status = 0
		self.vibrator_on = False
		self.ip = ""
		self.port = 51234
		self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serversocket.bind((str(self.ip), int(self.port)))
		self.serversocket.listen(5)
		self.clientsocket, self.addr = self.serversocket.accept()
		self.clientsocket.setblocking(0)
		self.tock = time.time()
		self.tock1 = time.time()
		# self.connection = sqlite3.connect('database.db')
		# self.cursor = self.connection.cursor()
