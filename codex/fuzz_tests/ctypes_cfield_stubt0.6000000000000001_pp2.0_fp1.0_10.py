import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(object):
    def __init__(self):
        self.value = 3

def f():
    return 1

class Y(object):
    def __init__(self):
        self.value = 2
    def f(self):
        return 2

class Z(object):
    def __init__(self):
        self.value = 1
    def f(self):
        return 1
    def g(self):
        return 1

class A(object):
    def __init__(self):
        self.value = 1
    def f(self):
        return 2
    def g(self):
        return 2

# Test the CField type
assert type(S.x) is ctypes.CField
print(S.x)

# Test the _CData_retval_ attribute of ctypes.CField
assert S.x._CData_retval_ is int

# Test the _CData_output_ attribute of ctypes.CField
assert S.x._CData_output_ is ctypes.pointer(ctypes
