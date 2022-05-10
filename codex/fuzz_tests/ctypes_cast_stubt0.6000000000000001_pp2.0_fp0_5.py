import ctypes
ctypes.cast(id(a), ctypes.py_object).value

# this is a neat way to get the object from an id
a = [1,2,3,4]
id(a)
b = ctypes.cast(id(a), ctypes.py_object).value

# this is a neat way to get the object from an id
a = [1,2,3,4]
id(a)
b = ctypes.cast(id(a), ctypes.py_object).value
b

# you can also use hex(id(a))
a = [1,2,3,4]
id(a)
hex(id(a))

# but then you can't use ctypes.cast()
a = [1,2,3,4]
id(a)
hex(id(a))
ctypes.cast(hex(id(a)), ctypes.py_object).value

# using id() is better
a = [1,2,3,4]
id(a)
hex(id(a))
ctypes.cast(hex(id(
