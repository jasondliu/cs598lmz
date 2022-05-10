import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
import sys
sys.getsizeof(x)

#%%
x = 1
sys.getsizeof(x)

#%%
x = 1.0
sys.getsizeof(x)

#%%
x = 1 + 2j
sys.getsizeof(x)

#%%
x = 'a'
sys.getsizeof(x)

#%%
x = True
sys.getsizeof(x)

#%%
x = None
sys.getsizeof(x)

#%%
x = []
sys.getsizeof(x)

#%%
x = ()
sys.getsizeof(x)

#%%
x = {}
sys.getsizeof(x)

#%%
x = set()
sys.getsizeof(x)

#%%
x = frozenset()
sys.getsizeof(x)

#%%
x = range(10)
sys.getsizeof(x)

#%%
x = byt
