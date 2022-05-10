import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def load_lib(name):
    return ctypes.CDLL(name)

def load_func(lib, name, restype, *argtypes):
    func = lib[name]
    func.restype = restype
    func.argtypes = argtypes
    return func

# vim: tabstop=4 shiftwidth=4 expandtab softtabstop=4
