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

point = POINT(1, 2)
p = ctypes.POINTER(POINT)(point)
print(p.contents.x, p.contents.y)

# Test ctypes.c_char_p

s = b"hello"
p = ctypes.c_char_p(s)
print(p.value)

# Test ctypes.c_wchar_p

s = "hello"
p = ctypes.c_wchar_p(s)
print(p.value)

# Test ctypes.c_void_p

