import ctypes
# Test ctypes.CFUNCTYPE
def py_test_callback(a, b):
    print (a, b)

test_callback = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)(py_test_callback)
test = ctypes.c_void_p.in_dll(fake_llvm.llvm, 'test')
test_callback.argtypes = ctypes.c_void_p, ctypes.c_int, ctypes.c_int
test_callback(test, 1, 2)

# Test ctypes.c_struct
# Create C++ Class

class c_class(Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

c_class_p = ctypes.POINTER(c_class)

# Create Python Class
class Py_class(object):
    def __init__(self):
        self.a = 0
        self.b = 0

    def __str__(self):
        return "{} {}".format(self.
