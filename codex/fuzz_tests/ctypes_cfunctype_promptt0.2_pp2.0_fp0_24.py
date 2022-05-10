import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
cmp_func = CMPFUNC(func)
print cmp_func(1, 2)

# Test ctypes.POINTER
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

point = POINT(1, 2)
point_p = ctypes.pointer(point)
print point_p.contents.x
print point_p.contents.y

# Test ctypes.c_char_p
s = ctypes.c_char_p("hello world")
print s.value

# Test ctypes.c_wchar_p
s = ctypes.c_wchar_p(u"hello world")
print s.value

# Test ctypes.c_void_p
s = ctypes.c_void
