import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

class libusb_device_handle(ctypes.Structure):
    pass
class libusb_transfer(ctypes.Structure):
    pass
class libusb_context(ctypes.Structure):
    pass
class libusb_device(ctypes.Structure):
    pass
class libusb_config_descriptor(ctypes.Structure):
    pass
class libusb_interface_descriptor(ctypes.Structure):
    pass
class libusb_endpoint_descriptor(ctypes.Structure):
    pass
class libusb_interface(ctypes.Structure):
    pass

class libusb_transfer_cb_fn(ctypes.CFUNCTYPE):
    _fields_ = [('callback', ctypes.c_void_p), ('user_data', ctypes.c_void_p)]

#
# libusb_error
#

LIBUSB_SUCCESS = 0
LIBUSB_ERROR_IO = -1
LIBUSB_ERROR_INVALID_PARAM = -2
LIBUSB_ERROR_
