import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class MyInteger(ctypes.CField):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

# a structure much like 'timeval' in struct.py
class MyTimeval(ctypes.Structure):
    _fields_ = [('tv_sec', MyInteger('tv_sec')),
                ('tv_usec', MyInteger('tv_usec'))]
cla
