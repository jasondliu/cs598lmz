import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import datetime
import socket
import struct
import fcntl
import pwd
import grp

# import gi
# gi.require_version('Gtk', '3.0')
# from gi.repository import Gtk, Gio, Gdk, GdkPixbuf, GLib, GObject

try:
	import dbus
	import dbus.service
	import dbus.mainloop.glib
except:
	# print("DBus not found")
	dbus = None

# try:
	# import RPi.GPIO as GPIO
# except:
	# GPIO = None

# try:
	# from Adafruit_BME280 import *
# except:
	# BME280 = None

# try:
	# from Adafruit_BMP.BMP085 import BMP085
# except:
	# BMP085 = None

# try:
	# from Adafruit_BMP.BMP183 import BMP183
# except:
	
