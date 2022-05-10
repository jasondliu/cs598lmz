import ctypes
# Test ctypes.CFUNCTYPE
class A(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

class B(ctypes.Structure):
    _fields_ = [('b', ctypes.c_long), ('a', A)]

def f(x, y):
    return ctypes.byref(x) == ctypes.byref(y)

compare = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.POINTER(A), ctypes.POINTER(A))
my_compare = compare(f)

a = A(4)
b = B(5, a)
c = B(6, a)
print(my_compare(b.a, c.a))
print(my_compare(c.a, b.a))

# Test OP_BUILD_TUPLE and OP_BUILD_LIST with different number of items
def f(x, y):
    return (x, y, x)
print(f(1, 2))

# Test OP_BUILD_MAP
