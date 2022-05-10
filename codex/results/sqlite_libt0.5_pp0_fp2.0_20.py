import ctypes
import ctypes.util
import threading
import sqlite3
import logging
import sys
import os
import re
import socket
import time
import string
import traceback
import random
import tempfile
import base64
import subprocess
import threading
import urllib
import urllib2

class Thread(threading.Thread):
	def __init__(self, target, *args):
		self._target = target
		self._args = args
		threading.Thread.__init__(self)
	def run(self):
		self._target(*self._args)

class Logger(object):
	def __init__(self, filename, level):
		logging.basicConfig(filename=filename, level=level, format='%(asctime)s %(levelname)s %(message)s')
		self.logger = logging.getLogger('Logger')
		self.logger.info('Logger started.')
	def log(self, level, message):
		if level == 'info':
			self.logger.info(message)
		el
