import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import traceback

current_milli_time = lambda: int(round(time.time() * 1000))

class LibEpoll(object):
	"""docstring for LibEpoll"""
	def __init__(self):
		super(LibEpoll, self).__init__()
		libc = ctypes.CDLL(ctypes.util.find_library("c"))
		libepoll = ctypes.CDLL(ctypes.util.find_library("rt"))

		epfd = libc.socket(2, 1, 0)	# AF_INET, SOCK_STREAM, IPPROTO_TCP

		self.libc = libc
		self.libepoll = libepoll
		self.epfd = epfd
	
		self.struct_in = ctypes.structures.__getattr__("sockaddr_in")
		self.struct_in6 = ctypes.structures.__getattr__("sockaddr_in6")
		self.struct_epoll_event
