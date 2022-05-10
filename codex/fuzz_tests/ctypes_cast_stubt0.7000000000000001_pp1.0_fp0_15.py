import ctypes
ctypes.cast(0, ctypes.py_object).value

# we can also get the value of a pointer to a python integer:
ctypes.cast(id(0), ctypes.py_object).value

# but we can't get the value of a pointer to a C integer:
ctypes.cast(id(0), ctypes.py_object).value

# we can't even get the value of a pointer to a python string:
ctypes.cast(id("0"), ctypes.py_object).value
 
# we can get the value of a pointer to a C string though:
ctypes.cast(id(b"0"), ctypes.py_object).value

# and if we have a pointer to a python integer, we can get its value:
ctypes.cast(id(ctypes.py_object(0).value), ctypes.py_object).value

# and we can get the value of a pointer to a python string:
ctypes.cast(id(ctypes.py_object("0").value), ctypes.py_object).value

# but we can't get the
