import ctypes
# Test ctypes.CFUNCTYPE

def test_c_func_type():
    c_func_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
    func = c_func_type(lambda x: x)
    assert func(42) == 42

def test_c_func_type_with_argtypes():
    c_func_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int,
                                   argtypes = [ctypes.c_int])
    func = c_func_type(lambda x: x)
    assert func(42) == 42

def test_c_func_type_with_restype():
    c_func_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int,
                                   restype = ctypes.c_int)
    func = c_func_type(lambda x: x)
    assert func(42) == 42

def test_c_func_type_with_argtypes_and_restype
