import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def api_as_uint(args):
    if isinstance(args, list):
        return [api_as_uint(a) for a in args]
    if isinstance(args, ctypes.CField):
        return args.value
    return args
