import ctypes
ctypes.cast(0, ctypes.py_object).value

# TypeError: NULL pointer access

ctypes.cast(None, ctypes.py_object).value

# TypeError: NULL pointer access

ctypes.cast(0, ctypes.py_object)

# c_void_p(0)

ctypes.cast(None, ctypes.py_object)

# c_void_p(None)

ctypes.cast(0, ctypes.py_object).value = 'Hello'

# TypeError: NULL pointer access

ctypes.cast(None, ctypes.py_object).value = 'Hello'

# TypeError: NULL pointer access

ctypes.cast(0, ctypes.py_object).value = 1

# TypeError: NULL pointer access

ctypes.cast(None, ctypes.py_object).value = 1

# TypeError: NULL pointer access

ctypes.cast(0, ctypes.py_object).value = None

# TypeError: NULL pointer access

ctypes.cast(None, ctypes.
