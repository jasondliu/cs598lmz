import ctypes
import ctypes.util
import threading
import sqlite3
from datetime import datetime

class HidApi():
    """A simple class for accessing USB HID devices on linux"""
    def __init__(self):
        self.dll = None
        
    def open(self):
        """
        Loads the hidapi library, and opens a handle to the first device
        """
        
        hidapi_path = ctypes.util.find_library('hidapi')
        self.dll = ctypes.CDLL(hidapi_path)
        
        hid_open = self.dll.hid_open
        hid_open.restype = ctypes.c_void_p
        hid_open.argtypes = [ctypes.c_ushort, ctypes.c_ushort, ctypes.c_wchar_p]
        
        #open a handle to the first device
        #since none is passed for the last argument, we get the first
        #device if there are more than one attached
        self.device = hid_open(0, 0, None)
        
        #check the handle
        if(self.device ==
