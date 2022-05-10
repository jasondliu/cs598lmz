import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def func(arg):
    return arg

print func(42)

# Test ctypes.CFUNCTYPE(None, ctypes.c_int)

@ctypes.CFUNCTYPE(None, ctypes.c_int)
def func(arg):
    print arg

func(42)

# Test ctypes.CFUNCTYPE(ctypes.c_int)

@ctypes.CFUNCTYPE(ctypes.c_int)
def func():
    return 42

print func()

# Test ctypes.CFUNCTYPE(None)

@ctypes.CFUNCTYPE(None)
def func():
    print 42

func()

# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

@ctypes.CFUNCTYPE
