import ctypes
ctypes.cast(id(0), ctypes.py_object).value

#%%
import sys
sys.getrefcount(0)

#%%
class A:
    pass
a = A()
b = A()
a is b

#%%
a == b

#%%
a = [1, 2, 3]
b = [1, 2, 3]
a is b

#%%
a == b

#%%
a = 257
b = 257
a is b

#%%
a == b

#%%
a = 257; b = 257
a is b

#%%
a = 257; b = 257
a == b

#%%
a = 257; b = 257; c = 257
a is b is c

#%%
a = 257; b = 257; c = 257
a == b == c

#%%
a = 1000; b = 1000
a is b

#%%
a = 1000; b = 1000
a == b

#%%
a = 1000; b = 1000; c = 1000
a is b is c

#%%
