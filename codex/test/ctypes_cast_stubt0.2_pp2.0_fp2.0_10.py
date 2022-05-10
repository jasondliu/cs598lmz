import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 3

import sys

def _mimport(name, level=1):
    try:
        return __import__(name, globals(), level=level)
    except:
        return __import__(name, globals())

