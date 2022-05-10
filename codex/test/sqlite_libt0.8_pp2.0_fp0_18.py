import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os
import getpass
import json

SERVER_PORT_NUM = 10000

pthread_create = ctypes.CDLL(ctypes.util.find_library('pthread')).pthread_create

class Connection:
	def __init__(self,sock):
		self.sock = sock
		self.buf = bytes()
		self.msgs = []

	def read(self):
		data = self.sock.recv(4096)
		self.buf += data
		self.process_buf()

	def process_buf(self):
		pos = self.buf.find(b'\xff')
		while pos != -1:
			self.msgs.append(self.buf[:pos].decode('utf-8'))
			self.buf = self.buf[pos+1:]
			pos = self.buf.find(b'\xff')

