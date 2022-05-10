import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect for threading
import socket
import os
import subprocess
import sys
import time
import sqlite3

import jesd204b as j
import jesd204b.pll as pll

from . import libjesd
from . import libjesd_py

# The number of bytes we can receive without an overrun.  This is
# calculated by dividing the memory buffer by the number of bytes per
# sample and each lane.
MAX_BYTES_PER_RX = libjesd.MAX_SAMPLES_PER_FRAME * libjesd.FRAME_SIZE

# The number of bytes we can transmit without an underrun.  This is
# calculated by dividing the memory buffer by the number of bytes per
# sample and each lane.
MAX_BYTES_PER_TX = libjesd.MAX_SAMPLES_PER_FRAME * libjesd.FRAME_SIZE

# The number of bytes we can transmit at once.  This is calculated by
# dividing the memory buffer by the number of bytes per sample and each
# lane.
BU
