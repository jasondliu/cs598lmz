import ctypes
# Test ctypes.CFUNCTYPE, ctypes.c_int, ctypes.POINTER, ctypes.c_void_p

libc = ctypes.CDLL(None)

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
paramflags = (1, "arg1", 0),

# def myfunc(arg1):
#    return arg1

CMPFUNC = prototype(("myfunc", libc), paramflags)

def myfunc(arg1):
    return arg1

myfunc.restype = ctypes.c_int
myfunc.argtypes = [ctypes.c_int]

print myfunc(42)

# Test ctypes.c_char_p, ctypes.c_wchar_p

CMPFUNC = prototype(("myfunc", libc), paramflags)

def myfunc(arg1):
    return "a"

myfunc.restype = ctypes.c_char_p
myfunc.argtypes = [ctypes.c_int]

print myfunc(42
