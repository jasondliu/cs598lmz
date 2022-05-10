import ctypes
# Test ctypes.CFUNCTYPE

def func(a, b):
    return a + b

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
print(f(1, 2))

# Test ctypes.POINTER

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

p = POINT(1, 2)
pp = ctypes.POINTER(POINT)(p)
print(pp.contents.x, pp.contents.y)

# Test ctypes.c_char_p

s = b"abc"
ss = ctypes.c_char_p(s)
print(ss.value)

# Test ctypes.c_wchar_p

s = "abc"
ss = ctypes.c_wchar_p(s)
print(ss.value)

# Test ctypes.c_void_p

s = b"abc"
