import ctypes
import ctypes.util
import threading
import sqlite3
import logging
import time

from ctypes import c_int, c_uint, c_short, c_ushort, c_char, c_uchar, c_float, c_double, c_void_p, POINTER, pointer, string_at, cast, sizeof, addressof

from pyQPCR.lib.libusb1 import libusb1
from pyQPCR.lib.libusb1 import libusb1 as libusb
from pyQPCR.lib.libusb1 import USBError

from pyQPCR.lib.util import get_path

USB_ERROR_NOT_FOUND = libusb1.LIBUSB_ERROR_NOT_FOUND
USB_ERROR_BUSY = libusb1.LIBUSB_ERROR_BUSY
USB_ERROR_NO_DEVICE = libusb1.LIBUSB_ERROR_NO_DEVICE
USB_ERROR_NOT_SUPPORTED = libusb1.LIBUSB_ERROR_NOT_SUPPORTED
USB_ERROR_OTHER = libusb1.LIBUSB_ERROR_OTHER

lib_name = ctypes.util.find_
