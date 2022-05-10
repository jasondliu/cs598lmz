import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b, c):
    print a, b, c

# prototype of func
prototype = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int)

# convert func into a callable C function
cfunc = prototype(func)

# call cfunc
cfunc(1, 2, 3)

# Test ctypes.WINFUNCTYPE
# prototype of MessageBoxA
prototype = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int)

# load user32.dll and get MessageBoxA
MessageBoxA = ctypes.windll.user32.MessageBoxA

# convert MessageBoxA into a callable C function
cfunc = prototype(MessageBoxA)

# call cfunc
cfunc(0, "Hello", "World", 0)
# Test ctypes.PYFUNCTYPE
# prototype of func

