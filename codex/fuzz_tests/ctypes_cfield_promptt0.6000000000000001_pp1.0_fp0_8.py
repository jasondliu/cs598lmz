import ctypes
# Test ctypes.CField.from_address()
libc = ctypes.CDLL(None)
class c_fun(ctypes.Structure):
    _fields_ = [
        ('cbuf', ctypes.c_char * 256),
        ('nargs', ctypes.c_int)
    ]

c_fun_p = ctypes.POINTER(c_fun)

def foo(x, y):
    pass

c_foo = c_fun_p.from_address(ctypes.addressof(foo))

print(c_foo.contents.cbuf)
print(c_foo.contents.nargs)

# Test ctypes.CField.from_address() with an integer
# address of a structure
class c_fun_p_int(ctypes.Structure):
    _fields_ = [
        ('cbuf', ctypes.c_char * 256),
        ('nargs', ctypes.c_int)
    ]

c_foo_int = c_fun_p_int.from_address(ctypes.addressof(foo))

