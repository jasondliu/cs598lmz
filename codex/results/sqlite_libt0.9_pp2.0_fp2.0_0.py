import ctypes
import ctypes.util
import threading
import sqlite3
import time
import ConfigParser
import platform
import re
import getopt
import sys

#For some reason, the libstdc++.so.6 is sometimes not properly imported
try:
    dll = ctypes.CDLL("libstdc++.so.6")
except:
    print("libstdc++ error")

#Import the Epics libraries
epics = ctypes.CDLL(ctypes.util.find_library("epics"))
epicsPv = ctypes.CDLL(ctypes.util.find_library("pv"))

#Import only the constants that we need
caget = epics.caget
caget.restype = ctypes.c_char_p
caget.argtypes = [ctypes.c_char_p]

ca_attach_context = epics.ca_attach_context
ca_attach_context.restype = ctypes.c_long
ca_attach_context.argtypes = []

ca_detach_context = epics.ca_detach_context
ca_detach_context.
