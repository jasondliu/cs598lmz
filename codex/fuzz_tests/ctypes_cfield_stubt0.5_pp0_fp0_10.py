import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(object):
    def get_x(self):
        return self.x

A.x = ctypes.CField()

a = A()
a.x = 5
print a.get_x()
</code>

