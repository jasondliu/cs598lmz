import ctypes
ctypes.cast(0, ctypes.py_object)

# This is a ctypes bug fixed in Python 3.2
# http://bugs.python.org/issue9291
# It is fixed in Python 2.7.3 and 3.2.3

# >>> import ctypes
# >>> ctypes.cast(0, ctypes.py_object)
# c_void_p(0)
# >>> ctypes.cast(0, ctypes.py_object).value
# Segmentation fault

# This is a ctypes bug fixed in Python 3.2
# http://bugs.python.org/issue9291
# It is fixed in Python 2.7.3 and 3.2.3

# >>> import ctypes
# >>> ctypes.cast(0, ctypes.py_object)
# c_void_p(0)
# >>> ctypes.cast(0, ctypes.py_object).value
# Segmentation fault

# This is a ctypes bug fixed in Python 3.2
# http://bugs.python.org/issue9291
# It is fixed in Python 2.7
