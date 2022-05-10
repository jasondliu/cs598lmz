import ctypes
ctypes.cast(id(0), ctypes.py_object).value

import sys
sys.getrefcount(0)

ctypes.cast(id(0), ctypes.py_object).value = 'whatever'

sys.getrefcount(0)

sys.getrefcount(1)

ctypes.cast(id(1), ctypes.py_object).value = 'whatever'

sys.getrefcount(1)

ctypes.cast(id(1), ctypes.py_object).value

ctypes.cast(id(0), ctypes.py_object).value

int.__new__(int)

int.__new__(int, 0)

int.__new__(int, 1)

