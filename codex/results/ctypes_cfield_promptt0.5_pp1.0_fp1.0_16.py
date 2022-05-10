import ctypes
# Test ctypes.CField
class c_test(ctypes.Structure):
    _fields_ = [('firstfield', ctypes.c_int),
                ('secondfield', ctypes.c_int)]

class c_test_subclass(c_test):
    _fields_ = [('thirdfield', ctypes.c_int)]

class c_test_subclass2(c_test):
    _fields_ = [('thirdfield', ctypes.c_int),
                ('fourthfield', ctypes.c_int)]

class c_test_subclass3(c_test):
    _fields_ = [('thirdfield', ctypes.c_int),
                ('fourthfield', ctypes.c_int),
                ('fifthfield', ctypes.c_int)]

class c_test_subclass4(c_test):
    _fields_ = [('thirdfield', ctypes.c_int),
                ('fourthfield', ctypes.c_int),
                ('fifthfield', ctypes.c_int),
                ('sixthfield', ctypes.c_int)]

class
