import ctypes
import ctypes.util
import threading
import sqlite3
import os, sys
import time
import datetime
import signal

import contrib.gc_collect as gc_collect

import contrib.py2 as py2
import contrib.py3 as py3


global_debug = True

def gdb_debug(fn):
	def wrapper(*args, **kwargs):
		if global_debug:
			sys.stderr.write('\nDebug:%s.%s()\n'%(fn.__module__, fn.__name__))
		ret = fn(*args, **kwargs)
		if global_debug:
			sys.stderr.write('Debug:exit %s.%s()\n\n'%(fn.__module__, fn.__name__))
		return ret

	return wrapper


def convert_timezone(t, new_zone='CST'):
	t_zone = t.tzinfo
	hour, minute = t_zone.utcoffset(t).seconds//3600, t_zone.utcoffset(t
