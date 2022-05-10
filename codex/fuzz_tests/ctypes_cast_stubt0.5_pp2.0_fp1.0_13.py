import ctypes
ctypes.cast(0, ctypes.py_object).value

# TypeError: NULL pointer access
ctypes.cast(None, ctypes.py_object).value

# TypeError: NULL pointer access
ctypes.cast(0, ctypes.c_int).value

# TypeError: NULL pointer access
ctypes.cast(0, ctypes.c_void_p).value

# TypeError: NULL pointer access
ctypes.cast(0, ctypes.c_char_p).value

# TypeError: NULL pointer access
ctypes.cast(0, ctypes.POINTER(ctypes.c_int)).contents

# TypeError: NULL pointer access
ctypes.cast(0, ctypes.POINTER(ctypes.c_char)).contents

# TypeError: NULL pointer access
ctypes.cast(0, ctypes.POINTER(ctypes.c_void_p)).contents

# TypeError: NULL pointer access
ctypes.cast(0, ctypes.POINTER(ctypes.py_object)).contents

# TypeError: NULL pointer access
ct
