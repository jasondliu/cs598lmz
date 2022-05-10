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
    else:
        print "OS not supported"
        exit()

    #
    # Set up the constants
    #
    HCI_CHANNEL_RAW = 0
    HCI_CHANNEL_USER = 1

    HCI_DEV_NONE = 0xffff
    HCI_MAX_DEV = 16
    HCI_MAX_ACL_SIZE = 1024
    HCI_MAX_SCO_SIZE = 255
    HCI_DEV_REG = 1
    HCI_DEV_UNREG = 2
    H
