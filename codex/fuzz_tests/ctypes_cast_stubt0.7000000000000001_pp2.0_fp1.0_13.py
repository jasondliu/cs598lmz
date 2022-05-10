import ctypes
ctypes.cast(0, ctypes.py_object)

import sys

sys.getrefcount(0)

a = 2
sys.getrefcount(a)

a = 'hello'
sys.getrefcount(a)

b = 'world'
sys.getrefcount(b)

a = 'world'
sys.getrefcount(a)

a = 'hello'
sys.getrefcount(a)

b = 'hello'
sys.getrefcount(b)

import gc

gc.get_threshold()
