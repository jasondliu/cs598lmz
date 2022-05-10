import ctypes
# Test ctypes.CFUNCTYPE
import ctypes

def func_callback(a, b, c):
    print "func_callback", a, b, c

CALLBACKFUNC = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int)

lib = ctypes.CDLL("./libfoo.so")
lib.test_callback.argtypes = (CALLBACKFUNC,)
lib.test_callback(CALLBACKFUNC(func_callback))

# Test ctypes.POINTER
import ctypes

class MyStruct(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int),]

lib = ctypes.CDLL("./libfoo.so")
lib.test_pointer.argtypes = (ctypes.POINTER(MyStruct),)
lib.test_pointer.restype = ctypes.POINTER(MyStruct)
result = lib.test_pointer(None)
print result.contents.a
print result.cont
