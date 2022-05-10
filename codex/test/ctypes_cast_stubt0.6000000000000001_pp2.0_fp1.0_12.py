import ctypes
ctypes.cast(1, ctypes.py_object)

# TypeError: an integer is required (got type str)
s = 'hello world'
ctypes.cast(s, ctypes.c_char_p)
