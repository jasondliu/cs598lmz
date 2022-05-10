import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
import sys

sys.getrefcount(x)

#%%
import ctypes

def ref_count(address: int):
    return ctypes.c_long.from_address(address).value

ref_count(id(x))

#%%
import weakref

a_set = {0, 1}
wref = weakref.ref(a_set)
wref

#%%
wref()

#%%
a_set = {2, 3, 4}
wref()

#%%
wref() is None

#%%
wref() is None

#%%
import sys

sys.getrefcount(a_set)

#%%
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
d['primary']


