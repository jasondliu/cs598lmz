import ctypes
ctypes.cast(id(int), ctypes.py_object).value

#%%
import sys
sys.getrefcount(1)

#%%
a = [1, 2, 3]
b = a
sys.getrefcount(a)

#%%
import ctypes
def ref_count(address: int):
    return ctypes.c_long.from_address(address).value
ref_count(id(a))

#%%
def ref_count(address: int):
    return ctypes.c_long.from_address(address).value
ref_count(id(a))

#%%
b = None
ref_count(id(a))

#%%
import weakref
a = [1, 2, 3]
b = weakref.ref(a)
b

#%%
b()

#%%
a = [1, 2, 3]
b = weakref.ref(a)
b()
a = None
b()

#%%
import weakref
a = [1, 2, 3]
b = weakref.ref(a)
