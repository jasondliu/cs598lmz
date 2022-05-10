import ctypes
ctypes.cast(0, ctypes.py_object).value

# this will cause a segfault
# ctypes.cast(0, ctypes.py_object).value = None

# this will cause a segfault
# ctypes.cast(0, ctypes.py_object).value = 0

# this will cause a segfault
# ctypes.cast(0, ctypes.py_object).value = 1

# this will cause a segfault
# ctypes.cast(0, ctypes.py_object).value = 2

# this will cause a segfault
# ctypes.cast(0, ctypes.py_object).value = 3

# this will cause a segfault
# ctypes.cast(0, ctypes.py_object).value = 4

# this will cause a segfault
# ctypes.cast(0, ctypes.py_object).value = 5

# this will cause a segfault
# ctypes.cast(0, ctypes.py_object).value = 6

# this will
