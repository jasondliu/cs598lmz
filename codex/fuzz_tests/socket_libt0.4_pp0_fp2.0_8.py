import socket
import time
import threading
import sys
import os
import re
import random
import string

from scapy.all import *

#/*******************************************************************************
# *
# * Global variables
# *
# ******************************************************************************/

#/*******************************************************************************
# *
# * Functions
# *
# ******************************************************************************/

#/*******************************************************************************
# *
# * Class definitions
# *
# ******************************************************************************/

class UDP_Client:
	"""
	"""
	def __init__(self, ip, port, data):
		self.ip = ip
		self.port = port
		self.data = data
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.settimeout(1)

	def send(self):
		self.sock.sendto(self.data, (self.ip, self.port))

class UDP_Server:
	"""
	"""
	def __init__(self, ip
