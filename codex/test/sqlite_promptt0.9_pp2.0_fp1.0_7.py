import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:/var/www/html/wlan_ref/wlan.db')
import time
import urllib.request

# Import the interface class
from accel import Accel
class AccelC(ctypes.Structure):
	"""Proxy of C struct AccelC"""
	__swig_setmethods__ = {"x" : _accel_accelc.__swig_setmethods__["x"].__func__, "y" : _accel_accelc.__swig_setmethods__["y"].__func__, "z" : _accel_accelc.__swig_setmethods__["z"].__func__}
	__setattr__ = lambda self, name, value: _swig_setattr(self, AccelC, name, value)
