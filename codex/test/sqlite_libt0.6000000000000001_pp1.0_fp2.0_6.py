import ctypes
import ctypes.util
import threading
import sqlite3
import ConfigParser
import os
import logging

#logging.basicConfig(level=logging.INFO)

class Spotify:
	libspotify = None
	session = None
	config = None
	appkey = None
	appkey_size = None

	def __init__(self, username, password, appkey_file, cache_location, settings_location, tracefile_location, user_agent):
		self.username = username
		self.password = password
		self.appkey_file = appkey_file
		self.cache_location = cache_location
		self.settings_location = settings_location
		self.tracefile_location = tracefile_location
		self.user_agent = user_agent
		self.session_callbacks = None
		self.session_userdata = None

		# Load libspotify
		self.libspotify = ctypes.CDLL(ctypes.util.find_library("spotify"))
