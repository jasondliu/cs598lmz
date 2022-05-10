import ctypes
# Test ctypes.CFUNCTYPE

def test_cfunctype(lib, func, restype, argtypes):
    f = ctypes.CFUNCTYPE(restype, *argtypes)(func)
    assert f(1, 2) == func(1, 2)

def test_cfunctype_errcheck(lib, func, restype, argtypes):
    def errcheck(result, func, args):
        return args[0] + args[1]

    f = ctypes.CFUNCTYPE(restype, *argtypes, errcheck=errcheck)(func)
    assert f(1, 2) == 3

def test_cfunctype_use_errno(lib, func, restype, argtypes):
    def use_errno(result, func, args):
        return args[0] + args[1]

    f = ctypes.CFUNCTYPE(restype, *argtypes, use_errno=True)(func)
    assert f(1, 2) == 3

def test_cfunctype_use_last_error(lib, func,
