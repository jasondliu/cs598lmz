import ctypes
# Test ctypes.CFUNCTYPE
CFUNCTYPE(c_int, c_int)(c_int(3))

# Test ctypes.POINTER(...)
POINTER(c_char)(c_char(97))

# Test ctypes.Structures
class Point(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int)]
a = Point(1, 2)
a.x = 3
# Test ctypes.Arrays
a = (c_int * 5)()
a[0] = 5
a[1] = 1

# Test ctypes.Union
class Value(Union):
    _fields_ = [("integer", c_int),
                ("pointer", c_void_p)]

# Test ctypes.CDLL
libc = CDLL("libc.so.6")
printf = libc.printf
printf("Hello %s!\n", "world")

# Test ctypes.string_at
string_at(c_char_p("Hello world"),5)
string_at(c_char_p("Hello world"),
