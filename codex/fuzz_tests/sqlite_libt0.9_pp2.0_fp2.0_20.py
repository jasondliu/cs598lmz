import ctypes
import ctypes.util
import threading
import sqlite3

# Preload sqlite3 module to make sqlite_version available after fork.
sqlite3

_libc_fdopen = ctypes.CDLL(ctypes.util.find_library('c')).fdopen

class StdStreamUnlocker(threading.Thread):
	"""Thread to allow restoring stdio streams after fork.

	Before starting this thread, prepare() should be called to
	prepare the descriptors to be used as new stdio streams.

	After starting this thread, start() should be called.  It
	closes all three pipes and replaces the corresponding standard
	streams with the new file descriptors.

	This is only necessary when using a ThreadPool executor that
	spawns processes.  For example, this happens when using the
	MPIPoolExecutor in mpi4py >= 3.0.0.
	"""
	def __init__(self, new_stdin, new_stdout, new_stderr):
		super(StdStreamUnlocker, self).__init__()
		self.new_stdin = new_stdin
