import ctypes
ctypes.cast(0, ctypes.py_object)

# TypeError: must be a ctypes type
ctypes.cast(0, object)

# TypeError: must be a ctypes type
ctypes.cast(0, "object")

# TypeError: must be a ctypes type
ctypes.cast(0, "ctypes.py_object")

# TypeError: must be a ctypes type
ctypes.cast(0, "ctypes.c_int")

# TypeError: must be a ctypes type
ctypes.cast(0, "ctypes.c_void_p")

# TypeError: must be a ctypes type
ctypes.cast(0, "ctypes.c_char_p")

# TypeError: must be a ctypes type
ctypes.cast(0, "ctypes.c_wchar_p")

# TypeError: must be a ctypes type
ctypes.cast(0, "ctypes.c_char")

# TypeError: must be a ctypes type
ctypes.cast(0, "ctypes.c_
