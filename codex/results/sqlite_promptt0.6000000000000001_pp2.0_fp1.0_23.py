import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')

class SecDNS(object):
    """
    SecDNS class
    """
    def __init__(self, libc_path=None):
        """
        Constructor
        """
        self._libc_path = libc_path or ctypes.util.find_library('c')
        self._libc = ctypes.CDLL(self._libc_path, use_errno=True)
        self._libc.gethostbyname_r.restype = ctypes.POINTER(ctypes.c_char)
        self._libc.gethostbyname_r.argtypes = [
            ctypes.c_char_p,  # name
            ctypes.POINTER(ctypes.c_char),  # hostent
            ctypes.c_char_p,  # buf
            ctypes.c_size_t,  # buflen
            ctypes.POINTER(ctypes.POINTER(ctypes.c_char)),  # result
            ctypes.POINTER(ctypes.c_int) 
