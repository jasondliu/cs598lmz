import ctypes
# Test ctypes.CFUNCTYPE
def test_cfunctype():
    # test return type
    for restype in [ctypes.c_int, ctypes.c_float, ctypes.c_double]:
        for argtypes in [[ctypes.c_int], [ctypes.c_int, ctypes.c_int],
                         [ctypes.c_float], [ctypes.c_float, ctypes.c_float],
                         [ctypes.c_double], [ctypes.c_double, ctypes.c_double]]:
            f = ctypes.CFUNCTYPE(restype, *argtypes)
            assert f.__name__ == 'CFUNCTYPE'
            assert f.__doc__ is None
            assert f.__module__ == 'ctypes'
            assert f.__dict__ == {}
            assert f.__defaults__ == None
            assert f.__kwdefaults__ == None
            assert f.__annotations__ == {}
            assert f.__code__ is None
            assert f.__globals__ is None
            assert f.__closure
