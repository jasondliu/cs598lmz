import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
from os.path import dirname, abspath, join as pjoin

import psmic
import psmic.display
import psmic.listview

from psmic.preferences_control import PreferencesControl

#require Qt5
import PyQt5.QtWidgets as pyqt5
import PyQt5.QtCore as qtc

#constants
BUS_ADDR_FORMAT_STRING = "0x{0:02X}"
BUS_ADDR_MIN_VALUE = 0
BUS_ADDR_MAX_VALUE = 127
START_BYTE_FORMAT_STRING = "{0:02X}"
START_BYTE_MIN_VALUE = 0
START_BYTE_MAX_VALUE = 255

