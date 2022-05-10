import ctypes
ctypes.cast(id(0), ctypes.py_object).value

import sys
sys.getrefcount(1)

a = [1, 2, 3]
b = a
sys.getrefcount(a)

a = None
sys.getrefcount(a)

import weakref
a_id = id(a)
