import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_call_fun():
    assert fun() is None

def test_call_fun_with_arg():
    assert fun(None) is None

def test_call_fun_with_kw():
    assert fun(x=None) is None

def test_call_fun_with_arg_and_kw():
    assert fun(None, x=None) is None

def test_call_fun_with_varargs():
    assert fun(None, None) is None

def test_call_fun_with_varargs_and_kw():
    assert fun(None, None, x=None) is None

def test_call_fun_with_varargs_and_kwargs():
    assert fun(None, None, x=None, **{}) is None

def test_call_fun_with_varargs_and_kwargs_and_kw():
    assert fun(None, None, x=None, **{}, y=None) is None

def test_call_fun_with_kwargs():
    assert fun(**
