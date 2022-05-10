import ctypes
ctypes.cast(0, ctypes.py_object)

# issue #2886
ctypes.string_at(0)
ctypes.string_at(0, 0)
ctypes.cast(0, ctypes.c_char_p).value

# issue #2983
libm = ctypes.CDLL(ctypes.util.find_library("m"))
libm.ceil(-1.5)
