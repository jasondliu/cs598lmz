import ctypes
import ctypes.util
import threading
import sqlite3
import time
import collections
import zlib
import shutil
import os

# TODO:
# - move this to a config file
# - make sure to add the "shared" directory to the PYTHONPATH environment variable
# - make sure to copy the "config.example.py" file to "config.py" and configure it
import config

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

_lock = threading.Lock()

def _with_lock(func):
	def _wrapped(*args, **kwargs):
		_lock.acquire()
		try:
			return func(*args, **kwargs)
		finally:
			_lock.release()
	return _wrapped

class InvalidRequest(Exception):
	pass

class InvalidResponse(Exception):
	pass

class CommandNotSupported(Exception):
	pass

class Request(object):

	def __init__(self, command, params, **kwargs):
		self.command
