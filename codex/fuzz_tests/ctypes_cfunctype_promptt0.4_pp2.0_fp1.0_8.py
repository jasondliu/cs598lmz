import ctypes
# Test ctypes.CFUNCTYPE()
CFUNCTYPE = ctypes.CFUNCTYPE

@CFUNCTYPE(None)
def func():
    pass

# Test ctypes.POINTER()
POINTER = ctypes.POINTER

@POINTER(ctypes.c_int)
def func():
    pass

# Test ctypes.byref()
byref = ctypes.byref

@byref
def func():
    pass

# Test ctypes.addressof()
addressof = ctypes.addressof

@addressof
def func():
    pass

# Test ctypes.cast()
cast = ctypes.cast

@cast(ctypes.c_int, ctypes.c_int)
def func():
    pass

# Test ctypes.memset()
memset = ctypes.memset

@memset(ctypes.c_int, 0, 1)
def func():
    pass

# Test ctypes.memmove()
memmove = ctypes.memmove

@memmove(ctypes.c_int
