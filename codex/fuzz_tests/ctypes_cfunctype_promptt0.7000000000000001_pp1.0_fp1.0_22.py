import ctypes
# Test ctypes.CFUNCTYPE
@CFUNCTYPE(c_int, c_int)
def add(a, b):
    return a + b

add(1, 2)
# Test ctypes.c_int
# The c_int is a C int, and the ctypes.sizeof() gives the size of the object 
# in bytes
c_int(42)
ctypes.sizeof(c_int)
# Test struct
class Point(Structure):
    _fields_ = [('x', c_int), ('y', c_int)]

Point(1, 2)
# Test create_string_buffer
s = create_string_buffer(b"Hello, World", 50)
s.value
# Test cast
cast(s, POINTER(c_char))[0]
# Test string_at
string_at(s)
# Test POINTER
p = cast(b"Hello, World", POINTER(c_char))
p[0]
# Test byref
byref(c_int(1))
