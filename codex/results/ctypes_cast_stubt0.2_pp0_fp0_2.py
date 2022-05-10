import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
import sys
sys.getsizeof(x)

#%%
x = 10
id(x)

#%%
x = x + 1
id(x)

#%%
x = 10
y = 10
id(x) == id(y)

#%%
x = 257
y = 257
id(x) == id(y)

#%%
x = 257; y = 257
id(x) == id(y)

#%%
x = 10; y = x
id(x) == id(y)

#%%
x = 10; y = x; x = 5
id(x) == id(y)

#%%
x = 10; y = x; x += 5
id(x) == id(y)

#%%
x = 10; y = x; x = x + 5
id(x) == id(y)

#%%
x = 10; y = x; x = x + 1
id(x) == id(y)

#
