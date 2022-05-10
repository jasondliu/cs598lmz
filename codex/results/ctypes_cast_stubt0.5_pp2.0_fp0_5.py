import ctypes
ctypes.cast(0, ctypes.py_object).value

# 'int' object is not callable
# ctypes.cast(0, ctypes.py_object)()

ctypes.cast(id(0), ctypes.c_void_p).value

ctypes.cast(0, ctypes.c_void_p).value

# TypeError: an integer is required
# ctypes.cast(None, ctypes.c_void_p)

import sys
ctypes.cast(id(sys.stdout), ctypes.c_void_p).value

ctypes.cast(id(sys), ctypes.c_void_p).value

ctypes.cast(id(object), ctypes.c_void_p).value

# ctypes.cast(0, ctypes.py_object).value

# TypeError: an integer is required
# ctypes.cast(None, ctypes.py_object)

# TypeError: an integer is required
# ctypes.cast(None, ctypes.py_object).value

# TypeError: an integer is
