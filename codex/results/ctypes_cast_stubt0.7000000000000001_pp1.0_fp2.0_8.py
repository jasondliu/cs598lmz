import ctypes
ctypes.cast(id(x), ctypes.py_object).value

import sys
sys.getrefcount(x)

#%% Reference counting and circular references
import ctypes
ctypes.cast(id(x), ctypes.py_object).value

import weakref
a_set = {0, 1}
wref = weakref.ref(a_set)
wref
wref()
a_set = {2, 3, 4}
wref()

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
d['primary']

del a
d['primary']

class Cheese:
    def __init__(self, kind):
        self.kind = kind
    def __repr__(self):
        return 'Cheese(%r)' % self.kind

import weakref
stock = weakref.WeakValueDictionary()
catalog
