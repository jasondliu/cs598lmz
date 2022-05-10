import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __getattribute__(self, name):
        if name == 'x':
            raise AttributeError
        return ctypes.Structure.__getattribute__(self, name)

class S3(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __setattr__(self, name, value):
        if name == 'x':
            raise AttributeError
        return ctypes.Structure.__setattr__(self, name, value)

class S4(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __delattr__(self, name):
        if name == 'x':
            raise AttributeError
        return ctypes.Structure.__delattr__(self, name)

class S5(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def
