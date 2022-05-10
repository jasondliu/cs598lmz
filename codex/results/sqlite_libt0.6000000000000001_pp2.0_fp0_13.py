import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys

try:
    from Queue import Queue  # Python 2.x
except ImportError:
    from queue import Queue  # Python 3.x

import pygatt
from pygatt.exceptions import NotConnectedError

import numpy as np
from scipy import signal

from matplotlib import pyplot as plt
from matplotlib import animation

# MAC address of the device.
device_mac_address = 'F5:10:3C:06:0A:44'

# UUIDs of the characteristics to access.
ECG_UUID = '0000fff1-0000-1000-8000-00805f9b34fb'
ACC_UUID = '0000fff2-0000-1000-8000-00805f9b34fb'

# Characteristic handle.
ECG_HANDLE = '0x0012'
ACC_HANDLE = '0x0015'

# Database file
db_file = 'data.db'

# Plot variables
plot_history_secs = 3
plot_
