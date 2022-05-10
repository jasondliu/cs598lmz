import ctypes
import ctypes.util
import threading
import sqlite3
import os, sys, json
import logging
from struct import *
from time import sleep
from Queue import Queue
from hashlib import sha1

if os.name == 'nt':
	import msvcrt
	from ctypes import windll, create_string_buffer

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger('winshare-client')

class FileTransferStatus:
	def __init__(self, filename, size, type, hash, peers):
		self.filename = filename
		self.size = size
		self.type = type
		self.hash = hash
		self.peers = peers

class TransferCommand:
	PING = 0
	SEARCH = 1
	SHARE_ADD = 2
	SHARE_REMOVE = 3
	SHARE_LIST = 4
	DOWNLOAD = 5
	DOWNLOAD_INFO = 6
	DOWNLOAD_PART = 7
	DOWNLOAD
