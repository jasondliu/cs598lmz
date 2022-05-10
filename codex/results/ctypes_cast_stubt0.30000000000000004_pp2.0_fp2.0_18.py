import ctypes
ctypes.cast(1, ctypes.py_object)

import sys
sys.getrefcount(1)

a = 'abc'
sys.getrefcount(a)

b = a
sys.getrefcount(a)

c = b
sys.getrefcount(a)

del a
sys.getrefcount(b)

del b
sys.getrefcount(c)

del c

import weakref
a = 'abc'
r = weakref.ref(a)
r()

del a
r()

a = 'abc'
r = weakref.ref(a)
r()

a = 'xyz'
r()

import gc
gc.collect()

r()

a = 'abc'
r = weakref.ref(a)
r()

a = 'xyz'
r()

a = 'abc'
r()

del a
r()

import weakref
a = 'abc'
r = weakref.ref(a)
r()

a = 'xyz'
r()
