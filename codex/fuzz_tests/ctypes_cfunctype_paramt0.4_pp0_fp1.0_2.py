import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def test_func(x):
    return x

def test_func_ptr():
    return FUNTYPE(test_func)

def test_func_ptr_call(x):
    return test_func_ptr()(x)

def test_func_ptr_call_2():
    f = test_func_ptr()
    return f(42)

def test_func_ptr_call_3():
    f = test_func_ptr()
    return f(f(42))

def test_func_ptr_call_4():
    f = test_func_ptr()
    return f(f(f(42)))

def test_func_ptr_call_5():
    f = test_func_ptr()
    return f(f(f(f(42))))

def test_func_ptr_call_6():
    f = test_func_ptr()
    return f(f(f(f(f(42)))))

def test_func_ptr_call_7():
