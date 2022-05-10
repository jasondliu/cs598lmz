import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import datetime
import subprocess
import shutil
import signal
import getopt
import json
import re

class unix_dbus_object(object):
	def __init__(self, bus_name, object_path, interface_name):
		self.bus_name = bus_name
		self.object_path = object_path
		self.interface_name = interface_name

	def get_object(self):
		return dbus.SessionBus().get_object(self.bus_name, self.object_path)

	def get_interface(self):
		return dbus.Interface(self.get_object(), self.interface_name)

class unix_dbus_service(unix_dbus_object):
	def __init__(self, bus_name, object_path, interface_name):
		unix_dbus_object.__init__(self, bus_name, object_path, interface_name)

	def get_service(self):
		return dbus.Session
