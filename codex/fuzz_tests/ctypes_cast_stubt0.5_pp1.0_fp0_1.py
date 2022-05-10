import ctypes
ctypes.cast(0, ctypes.py_object).value

class PyObject(ctypes.Structure):
    _fields_ = [("refcnt", ctypes.c_long)]

l = [1, 2, 3]
d = {'a': 1, 'b': 2}
s = 'abc'

print(PyObject.from_address(id(l)).refcnt)
print(PyObject.from_address(id(d)).refcnt)
print(PyObject.from_address(id(s)).refcnt)

import sys
sys.getrefcount(1)

a = [1, 2, 3]
b = a
print(sys.getrefcount(a))

import weakref
a = [1, 2, 3]
print(sys.getrefcount(a))
b = weakref.ref(a)
print(sys.getrefcount(a))
print(b)
print(b())
a = None
print(b)
print(b())

import gc
gc.collect()

gc.isenabled()

