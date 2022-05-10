import ctypes
ctypes.cast(0, ctypes.py_object).value

#%%
from ctypes import *

#%%
x = c_int(5)

#%%
print(x)

#%%
print(x.value)

#%%
x.value = 3

#%%
print(x.value)

#%%
x = c_double(5.0)

#%%
print(x.value)

#%%
x.value = 3.14

#%%
print(x.value)

#%%
x = c_float(2.5)

#%%
print(x.value)

#%%
x.value = 3.14

#%%
print(x.value)

#%%
x = c_long(1)

#%%
print(x.value)

#%%
x.value = 2147483647

#%%
print(x.value)

#%%
x.value = 2147483648

#%%
print(x.value)

#%%
x = c_
