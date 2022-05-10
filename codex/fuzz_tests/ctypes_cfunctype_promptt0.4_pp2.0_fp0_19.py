import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
cmp_func = CMPFUNC(func)

# Test ctypes.POINTER
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

point = POINT(1, 2)
point_ptr = ctypes.POINTER(POINT)(point)

# Test ctypes.c_buffer
buf = ctypes.create_string_buffer(b"Hello World")

# Test ctypes.c_char_p
char_p = ctypes.c_char_p(b"Hello World")

# Test ctypes.c_wchar_p
wchar_p = ctypes.c_wchar_p("Hello World")

# Test ctypes.c_void_p
void_p = ctypes.c_void_p()
