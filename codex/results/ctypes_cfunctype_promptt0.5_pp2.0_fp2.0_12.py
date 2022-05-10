import ctypes
# Test ctypes.CFUNCTYPE
def func(x, y):
    return x + y

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
cmp_func = CMPFUNC(func)

if cmp_func(1, 2) != 3:
    raise Exception("CFUNCTYPE test failed")

# Test ctypes.c_bool
if ctypes.c_bool(1) != True:
    raise Exception("c_bool test failed")

# Test ctypes.c_wchar
if ctypes.c_wchar('a') != 'a':
    raise Exception("c_wchar test failed")

# Test ctypes.c_char
if ctypes.c_char('a') != 'a':
    raise Exception("c_char test failed")

# Test ctypes.c_byte
if ctypes.c_byte(1) != 1:
    raise Exception("c_byte test failed")

# Test ctypes.c_ubyte
if ctypes.c_
