import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time

class Photon:
	def __init__(self, callbacks, library_path=None):
		if not library_path:
			library_path = ctypes.util.find_library('photon')
		if not library_path:
			raise Exception('Photon library not found.')
		self.__lib = ctypes.cdll.LoadLibrary(library_path)
		self.__lib.photon_init.restype = ctypes.c_int
		self.__lib.photon_init.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
		self.__lib.photon_init_socket.restype = ctypes.c_int
		self.__lib.photon_init_socket.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
		self.__lib.photon_start.restype = ctypes
