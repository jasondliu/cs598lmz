import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def test_function_ptr(lib):
    func = FUNTYPE(lib.test_function_ptr)
    assert func(5) == 5

def test_function_ptr_null(lib):
    func = FUNTYPE(lib.test_function_ptr_null)
    assert func(5) == 5

def test_function_ptr_null_arg(lib):
    func = FUNTYPE(lib.test_function_ptr_null_arg)
    assert func(5) == 5

def test_function_ptr_null_arg_err(lib):
    func = FUNTYPE(lib.test_function_ptr_null_arg_err)
    raises(ValueError, func, 5)

def test_function_ptr_arg_err(lib):
    func = FUNTYPE(lib.test_function_ptr_arg_err)
    raises(TypeError, func, 5)

def test_function_ptr_arg_err2(lib):
    func = FUNTYPE(lib.test_function_ptr
