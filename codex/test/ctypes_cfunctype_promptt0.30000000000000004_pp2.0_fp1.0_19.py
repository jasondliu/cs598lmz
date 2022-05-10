import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

func_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
func_c = func_type(func)

print(func_c(1, 2))

# Test ctypes.POINTER
class Foo(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

foo = Foo(1, 2)
foo_p = ctypes.POINTER(Foo)
foo_p_c = foo_p(foo)

print(foo_p_c.contents.x)
print(foo_p_c.contents.y)

# Test ctypes.cast
foo_p_c = ctypes.cast(foo_p_c, ctypes.c_void_p)
print(foo_p_c)

# Test ctypes.addressof
foo_p_c = ctypes.addressof(foo)
