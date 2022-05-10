import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_call_cfunc():
    assert fun() == 42

def test_call_cfunc_with_args():
    raises(TypeError, fun, 42)

def test_call_cfunc_with_kwargs():
    raises(TypeError, fun, foo=42)

def test_call_cfunc_too_many_args():
    raises(TypeError, fun, 42, 42)

def test_call_cfunc_too_many_kwargs():
    raises(TypeError, fun, foo=42, bar=42)

def test_call_cfunc_wrong_result_type():
    @FUNTYPE
    def fun():
        return 42.0
    raises(TypeError, fun)

def test_call_cfunc_wrong_arg_type():
    @FUNTYPE
    def fun(x):
        return x
    raises(TypeError, fun, 42.0)

def test_call_cfunc_wrong_arg_type_2():
    @FUNTYPE
    def fun(x):
        return
