import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import time

from . import keymap
from . import keyname
from . import keypress

# Create a ctypes.Structure subclass for each xcb_event_t struct
# that we need.  These are used to hold the events that we read
# from the X server.

class xcb_generic_event_t(ctypes.Structure):
	_fields_ = [("response_type", ctypes.c_uint8),
		("pad0", ctypes.c_uint8),
		("sequence", ctypes.c_uint16),
		("pad", ctypes.c_uint32 * 7),
		("full_sequence", ctypes.c_uint32)]

class xcb_button_press_event_t(ctypes.Structure):
	_fields_ = [("response_type", ctypes.c_uint8),
		("detail", ctypes.c_uint8),
		("sequence", ctypes.c_uint16),
		("time", ctypes.c_uint32),
	
