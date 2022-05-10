import ctypes
import ctypes.util
import threading
import sqlite3
import time
import csv
import os
import sys

from pydbus import SystemBus
from gi.repository import GLib


class GattTool:

	def __init__(self):
		self.bus = SystemBus()
		self.mainloop = GLib.MainLoop()
		self.adapter = self.bus.get('org.bluez','/org/bluez/hci0')
		self.adapter.onInterfacesAdded = self.interfaces_added
		self.adapter.onInterfacesRemoved = self.interfaces_removed
		self.device_list = []
		self.device_list_lock = threading.Lock()
		self.service_list = []
		self.service_list_lock = threading.Lock()
		self.characteristic_list = []
		self.characteristic_list_lock = threading.Lock()
		self.descriptor_list = []
		self.descriptor_list_lock = threading.Lock()
		self
