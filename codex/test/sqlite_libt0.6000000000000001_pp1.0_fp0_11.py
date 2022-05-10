import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import sys

from ctypes import *

#
# This class is used to listen for and log bluetooth events from the kernel
#
class BTL:

    #
    # Load the correct bluetooth library depending on the OS
    #
    if sys.platform == 'linux2':
        libbt = ctypes.cdll.LoadLibrary("libbluetooth.so.3")
    elif sys.platform == 'darwin':
        libbt = ctypes.cdll.LoadLibrary("libbluetooth.dylib")
