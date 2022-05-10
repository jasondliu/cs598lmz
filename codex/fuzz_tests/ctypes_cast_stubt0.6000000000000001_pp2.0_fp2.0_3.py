import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

import sys

sys.getrefcount(obj)
