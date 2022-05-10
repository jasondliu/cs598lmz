import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import time
import re

LIBNAME = ctypes.util.find_library("usb-1.0")

if not LIBNAME:
    raise Exception("libusb not found")

libusb = ctypes.CDLL(LIBNAME)

# Values for enumeration
libusb.LIBUSB_CLASS_PER_INTERFACE = 0
libusb.LIBUSB_CLASS_AUDIO = 1
libusb.LIBUSB_CLASS_COMM = 2
libusb.LIBUSB_CLASS_HID = 3
libusb.LIBUSB_CLASS_PRINTER = 7
libusb.LIBUSB_CLASS_MASS_STORAGE = 8
libusb.LIBUSB_CLASS_HUB = 9
libusb.LIBUSB_CLASS_DATA = 10
libusb.LIBUSB_CLASS_WIRELESS = 0xe0
libusb.LIBUSB_CLASS_APPLICATION = 0xfe
libusb.LIBUSB_CLASS_VENDOR_SPEC = 0xff

# Descriptor types
libusb.LIBUSB_DT_DEVICE = 0x01
