import ctypes
# Test ctypes.CFUNCTYPE
#
# This test passes if it runs without crashing.

def get_method(lib, name):
    method = getattr(lib, name)
    method.restype = ctypes.c_int
    method.argtypes = ()
    return method

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.POINTER(X)),
                ]

lib = ctypes.CDLL(ctypes.util.find_library("m"))

print "call once"
get_method(lib, "puts")("Hello world")

print "call more than once"
for i in range(10):
    get_method(lib, "puts")("Hello world")

print "wrapping the c_int type"
get_method(lib, "putchar")(ord('h'))
get_
