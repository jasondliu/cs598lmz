import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
cmp_func = CMPFUNC(func)
print(cmp_func(3, 4))

# Test ctypes.POINTER
class Bar(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

bar = Bar(1, 2)
print(bar.a, bar.b)

BarPtr = ctypes.POINTER(Bar)
bar_ptr = BarPtr(bar)
print(bar_ptr.contents.a, bar_ptr.contents.b)

# Test ctypes.c_char_p
s = b"hello world"
s_p = ctypes.c_char_p(s)
print(s_p.value)

# Test ctypes.c_void_p
v_p = ctypes.c_void_p
