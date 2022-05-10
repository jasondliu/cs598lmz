import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import sys
import codecs

class PyAbx:
	def __init__(self,dbfile,tablefile,datafile,**args):
		#self.dbfile = dbfile
		#self.tablefile = tablefile
		#self.datafile = datafile
		self.libpath = args.get('libpath','/usr/lib/libabx.so')

		self.db = TableDB(dbfile)
		self.dataset = Dataset(datafile)

		self.lib = ctypes.CDLL(self.libpath)
		self.lib.abx_new.restype = ctypes.c_void_p
		self.lib.abx_init.argtypes = [ctypes.c_void_p,ctypes.c_char_p,ctypes.c_char_p,ctypes.c_char_p]
		self.lib.abx_test.argtypes = [ctypes.c_void_p,ctypes.c_char_p
