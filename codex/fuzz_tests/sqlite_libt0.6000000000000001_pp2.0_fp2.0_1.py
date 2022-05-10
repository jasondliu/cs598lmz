import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os

# from https://github.com/jcsaaddupuy/python-augeas
import augeas
import sys
sys.path.insert(0, 'python-augeas/src/')

class NetworkManager(object):
    def __init__(self, dbus_interface_info):
        self.bus = dbus.SystemBus()
        self.proxy = self.bus.get_object(dbus_interface_info[0], dbus_interface_info[1])
        self.dbus_interface = dbus.Interface(self.proxy, dbus_interface_info[2])
        self.dbus_properties_interface = dbus.Interface(self.proxy, 'org.freedesktop.DBus.Properties')

    def get_devices(self):
        return self.dbus_interface.GetDevices()

    def get_all_access_points(self):
        devices = self.get_devices()
        access_points = []
        for device in devices:
            access_points.extend(self
