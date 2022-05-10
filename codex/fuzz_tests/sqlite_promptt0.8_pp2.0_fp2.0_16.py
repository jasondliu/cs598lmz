import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("file::memory:?cache=shared")

lib = None
_lock = threading.Lock()

try:
	if os.name == "nt":
		lib = ctypes.windll.LoadLibrary("libsqlite3.dll")
	else:
		lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"), ctypes.RTLD_GLOBAL)
except OSError:
	# Assume that libsqlite3 is already linked to the python executable
	lib = None

if not lib:
	def pysqlite_busy(lib):
		return lambda lib, count: 0
else:
	def pysqlite_busy(lib):
		c_busy_handler = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int)
		def busy(lib, count):
			# Try again in 0.2 seconds
			return 0 if count < 5 else 1
		return c_busy
