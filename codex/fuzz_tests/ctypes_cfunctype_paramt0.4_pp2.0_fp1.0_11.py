import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

def f(x, y):
    return x + y

f_c = FUNTYPE(f)

print(f_c(1, 2))

# ctypes.c_char_p is a string
# ctypes.c_char is a single character
# ctypes.c_int is a signed integer
# ctypes.c_uint is an unsigned integer
# ctypes.c_long is a long integer
# ctypes.c_ulong is an unsigned long integer
# ctypes.c_float is a float
# ctypes.c_double is a double
# ctypes.c_longdouble is a long double
# ctypes.c_void_p is a void pointer

# ctypes.create_string_buffer(b"Hello, World", 32)
# ctypes.create_unicode_buffer("Hello, World")
# ctypes.c_buffer(b"Hello, World", 32)
# ctypes.c_wchar_p("Hello, World")


