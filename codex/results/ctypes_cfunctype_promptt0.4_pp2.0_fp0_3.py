import ctypes
# Test ctypes.CFUNCTYPE

def func(x, y):
    return x + y

func_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
func_ptr = func_type(func)

assert func_ptr(1, 2) == 3

# Test ctypes.POINTER

class Foo(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

foo = Foo(1)
foo_ptr = ctypes.POINTER(Foo)(foo)

assert foo_ptr.contents.x == 1

# Test ctypes.sizeof

assert ctypes.sizeof(Foo) == 4

# Test ctypes.string_at

assert ctypes.string_at(ctypes.addressof(foo), 4) == b'\x01\x00\x00\x00'

# Test ctypes.cast

assert ctypes.cast(foo_ptr, ctypes.c_void_p).value == ctypes.addresso
