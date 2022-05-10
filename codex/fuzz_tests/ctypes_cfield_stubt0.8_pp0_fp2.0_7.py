import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(object):
    def __init__(self):
        self.x = 4

    def __getattribute__(self, attr):
        # Call __getattribute__ again and check the type of the result
        # in order to trigger a TypeError
        self.abc.abc
        return type(self).__dict__[attr].__get__(self, type(self))

class C(A):
    a = ctypes.CField()

C()
