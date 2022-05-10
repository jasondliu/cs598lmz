import ctypes
# Test ctypes.CFUNCTYPE
@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def add_func(a, b):
    return a + b
add_func(1, 2)

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def sub_func(a, b):
    return a - b
sub_func(1, 2)

# Test ctypes.POINTER
a = ctypes.c_int(1)
a_ptr = ctypes.POINTER(ctypes.c_int)(a)
a_ptr.contents.value

# Test ctypes.c_void_p
a = ctypes.c_int(1)
a_ptr = ctypes.cast(ctypes.pointer(a), ctypes.c_void_p)
a_ptr.value

# Test ctypes.pythonapi
