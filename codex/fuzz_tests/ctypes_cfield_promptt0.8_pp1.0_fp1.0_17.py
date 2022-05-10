import ctypes
# Test ctypes.CField with an array of pointers as elements
libc = ctypes.CDLL(ctypes.util.find_library("c"))

class Test(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.POINTER(ctypes.c_int) * 3),
        ("b", ctypes.c_int),
        ]

libc.malloc.restype = ctypes.POINTER(Test)
p = libc.malloc(ctypes.sizeof(Test))

print p.contents
print p.contents.a
print p.contents.b
