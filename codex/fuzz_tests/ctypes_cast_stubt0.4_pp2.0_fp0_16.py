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
a_ref = weakref.ref(a)
a_ref()

a = [1, 2, 3]
b = a
a_ref()

a = None
a_ref()

a = [1, 2, 3]
b = a
a_ref()

del b
a_ref()

del a
a_ref()

import gc
gc.collect()
a_ref()

a = [1, 2, 3]
b = a
a_ref()

a = None
a_ref()

import gc
gc.collect()
a_ref()
