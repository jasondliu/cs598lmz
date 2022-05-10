import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField(ctypes.CField):
    def __new__(self, *args, **kwargs):
        return ctypes.CField(*args, **kwargs)
    def __init__(self, *args, **kwargs):
        pass

class S2(ctypes.Structure):
    _fields_ = [('x', CField(ctypes.c_int))]

class S3(ctypes.Structure):
    _fields_ = [('x', CField(ctypes.c_int))]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class S4(ctypes.Structure):
    _fields_ = [('x', CField(ctypes.c_int))]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class S5(ctypes.Structure):
    _fields_ = [('x', CField(ctypes.c_int))]

