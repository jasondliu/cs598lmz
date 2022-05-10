import ctypes
# Test ctypes.CFUNCTYPE in a function context.
def f():
    c_int = ctypes.c_int
    c_int_p = ctypes.POINTER(ctypes.c_int)
    CFUNCTYPE = ctypes.CFUNCTYPE
    libc = ctypes.CDLL(ctypes.util.find_library('c'))
    c_printf = CFUNCTYPE(c_int, ctypes.c_char_p)(('printf', libc))
    c_printf('Hello, world!\n')
f()

# Test ctypes.CFUNCTYPE in a class context.
class C(object):
    def __init__(self):
        c_int = ctypes.c_int
        c_int_p = ctypes.POINTER(ctypes.c_int)
        CFUNCTYPE = ctypes.CFUNCTYPE
        libc = ctypes.CDLL(ctypes.util.find_library('c'))
        c_printf = CFUNCTYPE(c_int, ctypes.c_char_
