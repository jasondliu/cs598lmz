import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
import sys

sys.getrefcount(x)

#%%
x = [1, 2, 3]

#%%
import ctypes

def ref_count(address: int):
    return ctypes.c_long.from_address(address).value

ref_count(id(x))

#%%
x = None

#%%
ref_count(id(x))

#%%
x = [1, 2, 3]
y = x

#%%
ref_count(id(x))

#%%
del x

#%%
ref_count(id(y))

#%%
import weakref

a_set = {0, 1}
wref = weakref.ref(a_set)
wref

#%%
a_set = {2, 3, 4}
wref()

#%%
wref() is None

#%%
wref() is None

#%%
a_set = {0, 1}
wref = weak
