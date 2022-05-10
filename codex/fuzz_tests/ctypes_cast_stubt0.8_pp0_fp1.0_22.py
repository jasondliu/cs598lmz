import ctypes
ctypes.cast(obj, ctypes.py_object).value

s = 'hello world'
a = ctypes.cast(id(s), ctypes.py_object).value
print(a)
# hello world
