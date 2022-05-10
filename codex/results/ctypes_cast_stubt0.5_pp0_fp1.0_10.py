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
a = weakref.ref(5)
print(a)

a()

import sys
sys.getrefcount(1)

a = [1,2,3]
sys.getrefcount(a)

b = a
sys.getrefcount(a)

del a
sys.getrefcount(b)

c = [b, b]
sys.getrefcount(b)

del c
sys.getrefcount(b)

import ctypes
ctypes.cast(id(b), ctypes.py_object).value

sys.getrefcount(b)

a = 5
sys.getrefcount(a)

