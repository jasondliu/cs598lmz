import ctypes
import ctypes.util
import threading
import sqlite3 as lite
import time
import sys
import os

# Global Variables  
# Serial
global SerialDevice
global baudrate
global serialTimeout
global ser

# SPI
global spi
global spiDevice
global spiMaxSpeed
global spiMaxSpiSpeed

# PID
global Kp
global Ki
global Kd

#SQlite
global con


# /////////////// USB Relay Control via libUSB //////////////////
# http://doc.aldebaran.robotique.fr/doc/2-9/naoqi/peopleperception/usbrelay-py.html
libusb = ctypes.cdll.LoadLibrary(ctypes.util.find_library('usb-1.0'))

USB_DIR_OUT = 0x00
USB_TYPE_CLASS = 0x00
USB_TIMEOUT = 5000
REQUEST_TYPE = USB_TYPE_CLASS | USB_DIR_OUT

def usb_open_device(vid, pid):
    ctx = libusb.libusb_init(None)
    if ctx == None:
        raise
