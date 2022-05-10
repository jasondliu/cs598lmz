import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("d:\\dataset.db")

class SysTimers(object):
    """
    SysTimers - Get timing information
    """

    # Reference: http://rhodesmill.org/brandon/2013/clock-resolution/
    def __init__(self):
        self.clocks_per_sec = 10**2
        self.clocks_per_msec = 10**3
        self.clocks_per_usec = 10**6
        self.clocks_per_nsec = 10**9
        self.clocks_per_counter = 1.

