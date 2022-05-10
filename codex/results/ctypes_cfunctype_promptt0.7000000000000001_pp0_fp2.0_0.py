import ctypes
# Test ctypes.CFUNCTYPE
c_int_p = ctypes.POINTER(ctypes.c_int)


def func(p):
    return p[0]


cf = ctypes.CFUNCTYPE(ctypes.c_int)(func)
a = ctypes.c_int(4)
assert cf(a) == a.value
assert cf(ctypes.addressof(a)) == a.value

# Test ctypes.c_void_p
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
x = X()
assert ctypes.c_void_p(x).value == ctypes.addressof(x)
assert ctypes.c_void_p(x).value == x._pointer()
assert ctypes.c_void_p(x.a).value == ctypes.addressof(x.a)

# Test ctypes.c_char_p
assert ctypes.c_char_p(b"hello").value == b"hello"
assert ctypes.c_char_p("hello
