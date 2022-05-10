import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFuncPtr(object):
    _fields_ = [('p', ctypes.CField)]

    def __init__(self, val):
        self.p = ctypes.cast(val, self.p._type_)

    def __call__(self, *args):
        return self.p(*args)

f = CFuncPtr(ctypes.pythonapi.PyCode_New)

code = f(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
print(code)

print(type(code))

import dis
dis.dis(code)
