import ctypes
ctypes.cast(id(0), ctypes.py_object).value

#%%
import sys
sys.getrefcount(0)

#%%
a = [1, 2, 3]
b = a
sys.getrefcount(a)

#%%
import weakref
a = [1, 2, 3]
