import ctypes
# Test ctypes.CField
class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
    b = ctypes.CField()

s = S()
print(s.a, s.b)

# Test ctypes.Array
class A(ctypes.Array):
    _type_ = ctypes.c_int
    _length_ = 2

a = A()
print(a, len(a))
a[0] = 1
a[1] = 2
print(tuple(a))

# Test ctypes.create_string_buffer
print(ctypes.create_string_buffer("0123456789", 5))

# Test ctypes.pythonapi
print(ctypes.pythonapi.Py_InitModule4("spam", None, "doc", None, 101))

# Test ctypes.POINTER
import sys
if sys.version_info[0] == 2:
    ctypes.pythonapi.Py_InitModule4("spam", None, "doc", None, 101)
elif sys.version_info[0
