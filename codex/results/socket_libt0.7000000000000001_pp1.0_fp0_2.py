import socket
import time
import threading
import os
from queue import Queue
import sys
import tkinter as tk
from functools import partial

class Receive():
	def __init__(self, server_ip, port):
		self.connect = False
		self.server_ip = server_ip
		self.port = port
		self.receive = ''
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.bind((self.server_ip, self.port))

	def receive_data(self):
		self.s.listen(5)
		self.conn, self.addr = self.s.accept()
		self.connect = True
		while self.connect == True:
			self.receive = self.conn.recv(1024)
			self.receive = self.receive.decode('ascii')
			if not self.receive:
				self.connect = False
	
