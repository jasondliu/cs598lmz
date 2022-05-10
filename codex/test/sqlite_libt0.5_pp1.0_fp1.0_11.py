import ctypes
import ctypes.util
import threading
import sqlite3
import json
import os
import sys
import signal
import time

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

import pydbus
from gi.repository import GLib

import bluetooth

from bluepy.btle import Scanner, DefaultDelegate

from gattlib import GATTRequester, GATTResponse

from . import constants
from . import util
from . import config
from . import database
from . import api

from .exceptions import *

# TODO: handle exceptions in all threads
# TODO: ensure all threads are stopped

class BluetoothLEManager(object):
	"""
	Manages Bluetooth LE devices.
	"""
	
	def __init__(self, bus, config_dir):
		self.bus = bus
		self.config_dir = config_dir
		
		self.db = database.Database(self.config_dir)
		
		self.api = api.API(self.db)
