import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def _test(*args):
    raise NotImplementedError

test = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int))(_test)

assert issubclass(test.argtypes[0], ctypes.CFUNCTYPE)
assert test.argtypes[0](None, None, None) is None

assert isinstance(test.argtypes[0](), ctypes.CFUNCTYPE)
assert isinstance(test.argtypes[0](None, None, None), ctypes.c_int)

# test default value
test = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.CFUNCTYPE(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.CFUNCTYPE(ctypes.c_int))), c
