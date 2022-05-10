import ctypes
ctypes.cast(0, ctypes.c_void_p)
ctypes.cast(0, ctypes.py_object)

# The behavior of the following should be the same as the above
ctypes.cast(0, object)
ctypes.cast(0, int)
ctypes.cast(0, type(None))

# None to c_char_p and None to c_wchar_p should give None back
ctypes.cast(None, ctypes.c_char_p)
ctypes.cast(None, ctypes.c_wchar_p)
