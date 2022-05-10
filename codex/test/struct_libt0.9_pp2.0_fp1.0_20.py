import _struct
import sys
import os
import threading
import time
import Queue

#对socket实现一个简单的封装，让socket支持链接超时，防止攻击机系统
class CLIENTSOCKET(socket.socket):
	def __init__(self, family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0):
		socket.socket.__init__(self, family, type, proto)
		self.settimeout(3)
		
	def connect(self, address):
		n = socket.socket.connect_ex(self, address)
		
		if n == 0:
			return
		
		elif n == 10060:
			raise RuntimeError("socket connect() timeout!")
			
