import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

obj = POINT(1,2)
print '%s %s' % (obj.x, obj.y)

# Test ctypes.CField
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_float),
                ("y", ctypes.c_float)]

obj = Point(1.0, 2.0)
print '%s %s' % (obj.x, obj.y)

# Test ctypes.c_char_p
obj = ctypes.c_char_p("hello")
print obj.value

# Test ctypes.c_wchar_p
obj = ctypes.c_wchar_p("hello")
print obj.value

# Test ctypes.POINTER(ctypes.c_char)
obj = ctypes.POINTER(ctypes.c_char)()
print obj

# Test ctypes
