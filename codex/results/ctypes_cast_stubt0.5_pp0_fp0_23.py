import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# The value of the object is the same as the original object.
obj == ctypes.cast(id(obj), ctypes.py_object).value

# The id of the value is the same as the original object.
id(obj) == id(ctypes.cast(id(obj), ctypes.py_object).value)

# The value is a new instance of the class.
obj is ctypes.cast(id(obj), ctypes.py_object).value

# The id is different.
id(obj) == id(ctypes.cast(id(obj), ctypes.py_object).value)
</code>

