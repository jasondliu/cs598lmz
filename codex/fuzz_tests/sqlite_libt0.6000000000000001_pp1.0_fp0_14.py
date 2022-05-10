import ctypes
import ctypes.util
import threading
import sqlite3
import os

from ctypes import *
from ctypes.wintypes import *

# Set up some ctypes stuff.

# Constants
FILE_DEVICE_UNKNOWN             = 0x00000022
FILE_ANY_ACCESS                 = 0
METHOD_BUFFERED                 = 0

# Define the various device type values.  Note that values used by Microsoft
# Corporation are in the range 0-32767, and 32768-65535 are reserved for use
# by customers.
FILE_DEVICE_HAL                 = 0x00000101
FILE_DEVICE_KSEC                = 0x00000102
FILE_DEVICE_VIDEO               = 0x00000103
FILE_DEVICE_MOUSE               = 0x00000104
FILE_DEVICE_KEYBOARD            = 0x00000105
FILE_DEVICE_AUDIO               = 0x00000106
FILE_DEVICE_PORT                = 0x00000107
FILE_DEVICE_SERIAL_MOUSE_PORT   = 0x00000108
FILE_DEVICE_SERIAL_PORT         = 0x000001
