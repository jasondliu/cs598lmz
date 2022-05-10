import ctypes
ctypes.cast(0, ctypes.py_object)

import sys
sys.getrefcount(None)

import gc
gc.get_referrers(None)

import weakref
