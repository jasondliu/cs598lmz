import ctypes
# Test ctypes.CFUNCTYPE

libm = ctypes.CDLL(ctypes.util.find_library("m"))

func = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)(("sin", libm))

print(func(1.0))

# Test ctypes.WINFUNCTYPE

user32 = ctypes.windll.user32
MessageBox = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p)(("MessageBoxA", user32))

MessageBox(0, b"Hello", b"title", 0)
