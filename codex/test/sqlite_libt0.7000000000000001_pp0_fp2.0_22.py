import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import logging
import socket
import urllib.request
import json

# from ctypes import *

if sys.platform == 'linux':
    libssl = ctypes.cdll.LoadLibrary(ctypes.util.find_library('ssl'))
    libcrypto = ctypes.cdll.LoadLibrary(ctypes.util.find_library('crypto'))
    libnetifaces = ctypes.cdll.LoadLibrary(ctypes.util.find_library('netifaces'))
elif sys.platform == 'darwin':
    libssl = ctypes.cdll.LoadLibrary(ctypes.util.find_library('ssl'))
    libcrypto = ctypes.cdll.LoadLibrary(ctypes.util.find_library('crypto'))
    libnetifaces = ctypes.cdll.LoadLibrary(ctypes.util.find_library('netifaces'))
