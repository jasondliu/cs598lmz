import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('db.sqlite3')

# Ctypes for libusb
_libusb = ctypes.CDLL(ctypes.util.find_library('usb-1.0'))
_libusb.libusb_init.restype = ctypes.c_void_p
_libusb.libusb_open_device_with_vid_pid.argtypes = [ctypes.c_void_p, ctypes.c_uint16, ctypes.c_uint16]
_libusb.libusb_open_device_with_vid_pid.restype = ctypes.c_void_p
_libusb.libusb_close.argtypes = [ctypes.c_void_p]
_libusb.libusb_get_device_descriptor.argtypes = [ctypes.c_void_p, ctypes.POINTER(libusb_device_descriptor)]
_libusb.libusb_get_device_descriptor.restype = ctypes.c_int
