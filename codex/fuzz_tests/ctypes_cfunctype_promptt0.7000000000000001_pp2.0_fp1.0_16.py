import ctypes
# Test ctypes.CFUNCTYPE
CFUNCTYPE = ctypes.CFUNCTYPE

@CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def func(a, b):
    return a + b

print func(1, 2)

# Test ctypes.py_object
py_object = ctypes.py_object

class A(object):
    def __init__(self):
        self.x = 1
        self.y = 2

a = A()

print a.x
print a.y

# Test ctypes.c_ubyte
c_ubyte = ctypes.c_ubyte

a = c_ubyte(0xff)
b = a.value

print a
print b

# Test ctypes.c_char_p
c_char_p = ctypes.c_char_p

a = c_char_p("abc")
b = a.value

print a
print b

# Test ctypes.c_void_p
c
