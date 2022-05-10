import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFunctionType(object):
    def __init__(self, restype, argtypes, callingconv=ctypes.c_int):
        self.restype = restype
        self.argtypes = argtypes
        self.callingconv = callingconv
    def __call__(self, name, library):
        return ctypes.CFUNCTYPE(self.restype, *self.argtypes)(
            name, library, self.callingconv)

class Lambda(object):
    def __init__(self, args, body):
        self.args = args
        self.body = body
    def __call__(self, *args):
        return self.body(*args)
