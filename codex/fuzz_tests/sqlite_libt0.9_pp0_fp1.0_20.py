import ctypes
import ctypes.util
import threading
import sqlite3
import sys

# rtlsdr constants:
# gain stuff:
RTLSDR_TUNER_GAIN_DEFAULT = -1
# timeout stuff:
POLL_TIMEOUT = 1000  # ms
# default sample rate. must be 2.4M or below
DEFAULT_SAMPLE_RATE = 2.4e6
# The rtl-sdr uses a sample rate of 2.4 MHz, 
# 2.4 MHz / 256 = 9375 or 0x2500
BUFFER_SIZE = 0x2500 * 16



libc = ctypes.CDLL(ctypes.util.find_library('c'))

class SDR(object):
    CONFIG = "SELECT * FROM config"
    SQL = dict(
        insert = "INSERT INTO sdr (id, timestamp, frequency, mode, sdr_data) VALUES (?, datetime('now', 'localtime'), ?, ?, ?)",
        update = "UPDATE sdr SET id = ?, timestamp = datetime('now', 'localtime'), frequency = ?, mode = ?, sdr_data = ? WHERE id =
