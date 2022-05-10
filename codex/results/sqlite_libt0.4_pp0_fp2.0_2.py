import ctypes
import ctypes.util
import threading
import sqlite3
import time
import datetime
import os
import sys
import logging
import logging.handlers

#
# Logging
#

logger = logging.getLogger('bluetooth_logger')
logger.setLevel(logging.DEBUG)

handler = logging.handlers.SysLogHandler(address = '/dev/log')

formatter = logging.Formatter('%(module)s.%(funcName)s: %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

#
# Constants
#

# TODO: determine these at runtime

# The maximum number of bytes that can be read in a single HCI packet
HCI_MAX_PACKET_SIZE = 255

# The number of bytes in a Bluetooth address
BDADDR_LEN = 6

# The number of bytes in an EIR data type
EIR_DATA_LEN = 2

# The number of bytes in an EIR data length
EIR_LENGTH_LEN = 1

# The maximum number of bytes
