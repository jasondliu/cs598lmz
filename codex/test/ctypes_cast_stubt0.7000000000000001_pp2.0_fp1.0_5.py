import ctypes
ctypes.cast(id(42), ctypes.py_object).value

#%%
a = 42
b = ctypes.cast(id(a), ctypes.py_object).value
print(a is b)

#%%
a = 42
b = ctypes.cast(id(a), ctypes.py_object).value
print(a, b)

#%%
a = 42
b = ctypes.cast(id(a), ctypes.py_object).value
print(a == b)

#%%
id(42)

#%%
id(42)

#%%
id(a)

#%%
id(b)

#%%
id(b)

#%%
