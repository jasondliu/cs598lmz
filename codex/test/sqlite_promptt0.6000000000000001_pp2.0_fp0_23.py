import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('data/dummy.db')
import time
import os

# import RPi.GPIO as GPIO

# Set up some constants
_I2C_READ = 1
_I2C_WRITE = 0

# Some helper functions
def reverseByteOrder(data):
    "Reverses the byte order of an int (16-bit) or long (32-bit) value"
    # Courtesy Vishal Sapre
    byteCount = len(hex(data)[2:].replace('L','')[::2])
    val       = 0
    for i in range(byteCount):
        val    = (val << 8) | (data & 0xff)
        data >>= 8
    return val

def getSMBus(bus = 1):
    "Returns a SMBus object for the specified bus"
    return SMBus(bus)

class SMBus(object):
    def __init__(self, bus = 1):
        self.fd = os.open("/dev/i2c-1", os.O_RDWR)

    def close(self):
        os
