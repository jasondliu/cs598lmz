import ctypes
# Test ctypes.CFUNCTYPE
cdll.msvcrt.printf(b"%s %s\n", ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)(b"Hello", b"World"))
