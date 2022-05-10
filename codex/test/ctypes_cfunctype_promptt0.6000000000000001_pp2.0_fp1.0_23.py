import ctypes
# Test ctypes.CFUNCTYPE.
def foo(n):
    return n+1
c_foo = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(foo)
print(c_foo(1))

# Test ctypes.POINTER.
