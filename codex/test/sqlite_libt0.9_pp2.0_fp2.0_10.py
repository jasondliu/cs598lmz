import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import tempfile
import re
import Queue
import cStringIO
import math

import traceback

from configobj import ConfigObj

import engine

from progress import Progress
from utilities import get_temp_dir

from imdb import IMDb

try:
	import json
except ImportError:
	import simplejson as json

#Check for Modules required for Win 7 serial support
try:
	import pywinusb
	pywinusb_failed = False
except ImportError:
	pywinusb_failed = True

try:
	import usb.core
	import usb.util
	pyusb_failed = False
except ImportError:
	pyusb_failed = True

try:
	import win32api
	import win32file
	import win32con
	win32api_failed = False
except ImportError:
	win32api_failed = True

#Definitions
#IMDB Movie Title Regular Expression
#IMDB Movie Title Regex: (.*) \(([0-9]{4})([\w\s\-,]*)(?:
