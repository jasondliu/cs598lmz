import ctypes
# Test ctypes.CFUNCTYPE
def func(x):
    return x * 2

CFunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
cfunc = CFunc(func)
print(cfunc(2))

# Test ctypes.POINTER
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

point = POINT(1, 2)
point_p = ctypes.POINTER(POINT)(point)
print(point_p.contents.x, point_p.contents.y)

# Test ctypes.c_char_p
c_char_p = ctypes.c_char_p("Hello")
print(c_char_p.value)

# Test ctypes.c_wchar_p
c_wchar_p = ctypes.c_wchar_p("你好")
print(c_wchar_p.value)

# Test ctypes.c_void_p
c
