import ctypes
import ctypes.util
import threading
import sqlite3
import os
import traceback
import sys

class DBusWrapper(object):
	_dbus_so = None
	_dbus_functions = {}
	def _dbus_init(self):
		if not DBusWrapper._dbus_so:
			dbus_so_name = ctypes.util.find_library("dbus-1")
			if not dbus_so_name:
				raise Exception("Unable to find dbus-1 library")
			DBusWrapper._dbus_so = ctypes.cdll.LoadLibrary(dbus_so_name)
			DBusWrapper._dbus_functions["dbus_connection_get_fd"] = DBusWrapper._dbus_so.dbus_connection_get_fd
			DBusWrapper._dbus_functions["dbus_connection_get_unix_fd"] = DBusWrapper._dbus_so.dbus_connection_get_unix_fd
			DBusWrapper._dbus_
