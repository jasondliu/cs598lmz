import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is the equivalent of
# ctypes.cast(id(0), ctypes.py_object).value
# which is not allowed by the interpreter.

# The following code snippet is equivalent to
# ctypes.cast(id(0), ctypes.py_object).value = "Hello"
ctypes.cast(id(0), ctypes.py_object).value = "Hello"

# The following code snippet is equivalent to
# ctypes.cast(id(0), ctypes.py_object).value = "Hello"
ctypes.cast(id(0), ctypes.py_object).value = "Hello"

# The following code snippet is equivalent to
# ctypes.cast(id(0), ctypes.py_object).value = "Hello"
ctypes.cast(id(0), ctypes.py_object).value = "Hello"

# The following code snippet is equivalent to
# ctypes.cast(id(0), ctypes.py_object).value = "Hello"
ctypes.cast(id(0),
