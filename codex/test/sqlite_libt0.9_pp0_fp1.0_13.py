import ctypes
import ctypes.util
import threading
import sqlite3
import pwd
import grp
import csv
import imp
import os, sys
import fcntl
import re
import stat

from system import device, system
import config

if ctypes.sizeof(ctypes.c_voidp) == 4:
	LIB = "wiringPi32.so"
	pi = device.Device("/dev/mem", 0x7E000000, 0x100, "wiringPi_io")
else:
	LIB = "wiringPi.so"
	pi = device.Device("/dev/mem", 0x3F000000, 0x100, "wiringPi_io")

lib = ctypes.cdll.LoadLibrary(LIB)

wave = None
wavechans = []

#db = sqlite3.connect("/var/lib/datadog/wifindin.db")
#dbc = db.cursor()
#db.text_factory = str

#dumpfile = open("/var/lib/datadog/dumpfile", "a+")

INT = ctypes.c_
