import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x**2

f = FUNTYPE(func)

print(f(2))

print(f(3))

#------------------------------------------------------------------------------
#   ctypes.c_bool
#------------------------------------------------------------------------------

print(ctypes.c_bool(True))

print(ctypes.c_bool(False))

print(ctypes.c_bool(1))

print(ctypes.c_bool(0))

#------------------------------------------------------------------------------
#   ctypes.c_char
#------------------------------------------------------------------------------

print(ctypes.c_char('a'))

print(ctypes.c_char('\n'))

print(ctypes.c_char(b'a'))

print(ctypes.c_char(b'\n'))

#------------------------------------------------------------------------------
#   ctypes.c_wchar
#------------------------------------------------------------------------------

print(ctypes.c_wchar('a'))

print(ctypes.c_wchar('\n'))

print
