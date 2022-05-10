import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import base64
import struct
import time

# TODO:
#
# 1. Add an option to flush the buffer after each command
#    (even if it's slow, it will be more bomb-proof)
# 2. Add a reset flag to the main loop, and add an option
#    that would cause it to reset the serial port in case
#    of frame errors.
# 3. Add support for x-on/x-off flow control.
# 4. Add a loopback test.  (You could set the buffer size
#    to 0, and get back the same data you sent.)
# 5. Add support for asynchronous reads.
# 6. Add support for non-blocking writes.
# 7. Add a config file to specify the default serial port,
#    baud rate, and data bits, parity, and stop bit settings.

# Frame format:
#
#   [SOH][SOH][ESC][ESC][TYPE][LEN][LEN][DATA][CRC]
#
#   SOH = start of header (0x01)
#  
