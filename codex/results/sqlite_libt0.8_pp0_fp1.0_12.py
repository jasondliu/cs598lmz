import ctypes
import ctypes.util
import threading
import sqlite3
import collections

try:
	import notifo2
except ImportError:
	notifo2 = None

if notifo2 is not None:
	try:
		notifo2.Notifo
	except AttributeError:
		notifo2 = None

def _dlopen(name, mode):
	if not name:
		return None
	path = ctypes.util.find_library(name)
	if not path:
		return None
	return ctypes.CDLL(path, mode)

_sqlite = _dlopen("sqlite3", ctypes.RTLD_GLOBAL | ctypes.RTLD_LAZY)
if not _sqlite:
	print >>sys.stderr, "error: unable to locate sqlite3 library"
	sys.exit(1)

_sqlite.sqlite3_open.argtypes = (ctypes.c_char_p,) * 2
_sqlite.sqlite3_open.restype = ctypes.c_int
_sqlite.sqlite3
