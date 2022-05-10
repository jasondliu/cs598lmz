import ctypes
import ctypes.util
import threading
import sqlite3
import sys
from debugger_pb2 import *
from console import *


libproc = ctypes.CDLL(ctypes.util.find_library('libproc'))
libproc.proc_exitstatus.restype = ctypes.c_int

class DebugTextDB:
	# db = None
	# cursor = None
	def __init__(self):
		self.db = sqlite3.connect("./debug.db")
		self.cursor = self.db.cursor()
		self.cursor.execute('''create table if not exists debug_value(
			system varchar(128),
			scenario varchar(128),
			process varchar(128),
			msg varchar(512),
			value int)
		''')
		self.cursor.execute('''create table if not exists debug_trace(
			system varchar(128),
			scenario varchar(128),
			process varchar(128),
	
