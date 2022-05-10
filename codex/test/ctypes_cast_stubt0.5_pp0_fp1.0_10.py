import ctypes
ctypes.cast(0, ctypes.py_object)

import sys
sys.getrefcount(None)

a = None
sys.getrefcount(None)

b = a
sys.getrefcount(None)

c = [b]
sys.getrefcount(None)

sys.getrefcount(1)
del a,b,c
sys.getrefcount(1)

import weakref
