import ctypes
ctypes.cast(id(0), ctypes.py_object).value

#%%
import sys
sys.getrefcount(0)

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
wref() is None

#%%
wref() is None

#%%
wref() is None

#%%
wref() is None

#%%
wref() is None

#%%
wref() is None

#%%
wref() is None

#%%
wref() is None

#%%
wref() is None

#%%
wref() is None

#%%
wref() is None

#%%
wref() is None

#%%
wref() is None

#%%
wref() is None

#%%
wref() is None

#
