import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

#%%
# 可以把对象的内存地址转换为整数：
obj = object()
print(id(obj))

#%%
# 可以把整数转换为对象：
obj = ctypes.cast(id(obj), ctypes.py_object).value
print(obj)

#%%
# 可以把对象的内存地址转换为整数：
obj = object()
print(id(obj))

#%%
# 可以把整数转换为对象：
obj = ctypes.cast(id(obj), ctypes.py_object).value
print(obj)

#%%
# 可以
