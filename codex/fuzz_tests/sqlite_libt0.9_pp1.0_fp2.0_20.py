import ctypes
import ctypes.util
import threading
import sqlite3
from hydrant import request as req
from hydrant import lineformat

__all__ = ( 'gettime', 'get_monotonic_time', 'readfile', 'readproc', 'Elapsed'
		  , 'Conf', 'Log', 'ConfSection', 'FILETYPE_CONFIG', 'FILETYPE_SQLITE'
		  , 'FILETYPE_PYTHON', 'FILETYPE_TEXT', 'LogFilters', 'LogFilter'
		  , 'ConfDefaults', 'LogDefaults')

(FILETYPE_CONFIG, FILETYPE_SQLITE, FILETYPE_PYTHON, FILETYPE_TEXT) = range(4)

def gettime(precision=6):
	"""
		Get the time in the format of 2015-11-22 14:26:58.350280.
		
		date, time
			output 		: date 2015-11-22 14:26:58.350280
			description	: return the current time in a tuple with
						  (date, time).
		

