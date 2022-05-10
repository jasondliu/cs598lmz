import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

import ctypes.test

class X(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

def check_paramflags(self, value, func, expected):
    func.restype = ctypes.c_void_p
    func.argtypes = (ctypes.POINTER(X),)
    flags = func(ctypes.pointer(value))
    self.failUnlessEqual(ctypes.c_int.from_address(flags).value, expected)

if __name__ == '__main__':
    from ctypes import *
    from test.test_support import run_unittest
    run_unittest(ctypes.test.test_paramflags)
    run_unittest(ctypes.test.test_paramflags2)
