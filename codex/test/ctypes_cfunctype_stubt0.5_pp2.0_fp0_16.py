import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_cfunc():
    f = fun
    assert f() == 1
    assert f.__name__ == 'fun'
    assert f.__doc__ is None

def test_cfunc_call():
    f = fun
    assert f() == 1
    raises(TypeError, "f(1)")
    raises(TypeError, "f(1,2)")

def test_cfunc_call_wrong_result():
    import ctypes
    f = ctypes.CFUNCTYPE(ctypes.c_int)(lambda: "hello")
    raises(TypeError, f)

def test_cfunc_call_wrong_arg():
    import ctypes
    f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x)
    raises(TypeError, f, "hello")

def test_cfunc_call_wrong_arg_2():
    import ctypes
