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
print point.x, point.y

point_pointer = ctypes.POINTER(POINT)
p = point_pointer(point)
print p.contents.x, p.contents.y

# Test ctypes.c_char_p
print ctypes.c_char_p("hello world")

# Test ctypes.c_wchar_p
print ctypes.c_wchar_p(u"hello world")

# Test ctypes.c_void_p
print ctypes.
