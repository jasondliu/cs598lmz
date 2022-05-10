import ctypes
import ctypes.util
import threading
import sqlite3
import os
import mmap
import time

from alarmdecoder import AlarmDecoder
from alarmdecoder.devices import USBDevice

class AlarmDecoder(object):
    """
    AlarmDecoder is a class that wraps the alarmdecoder library, providing a
    Pythonic interface to the AlarmDecoder alarm panel interface.

    Keyword arguments:
      device -- The device to use.  If a string is provided, it will be treated
        as a serial port.  If a list is provided, each element will be treated
        as a serial port.  The first serial port that responds to a query is
        the port that will be used.  If a USBDevice is provided, it will be used
        as the device.
    """

    def __init__(self, device=None):
        self._dev = None
        self._device = device
        self._loop_thread = None
        self._loop_thread_stop = None
        self._message_callback = None
        self._partition_callback = None
        self._zone_callback = None
        self._zone_timer_callback
