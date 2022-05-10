import ctypes
import ctypes.util
import threading
import sqlite3
import traceback
from xdg.BaseDirectory import xdg_cache_home
import os
import urllib
from gi.repository import GLib
from ConfigParser import ConfigParser
import copy
from utils import get_module_data_file

from utils import Logger
log = Logger("XS")

use_local_db = False


class XS(object):
	"""A singleton object to store data and make active requests to Last.fm"""
	def __init__(self):
		global use_local_db
		self.api_key = '2d646f5b0d1549573e24ec4f3e7d1d5e'
		self.api_url = 'http://ws.audioscrobbler.com/2.0/'
		self.audioscrobbler = None
		self.artwork_cache = {}
		# used to prevent multiple requests to last.fm at once
		self.lastfm_active_lock = threading.Lock() 
		self.
