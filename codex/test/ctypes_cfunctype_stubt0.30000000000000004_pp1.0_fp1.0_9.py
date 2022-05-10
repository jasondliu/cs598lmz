import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

def test_fun_call():
    assert call(fun) == "hello"

def test_fun_call_with_args():
    assert call(fun, 1, 2, 3) == "hello"

def test_fun_call_with_kwargs():
    assert call(fun, a=1, b=2, c=3) == "hello"

def test_fun_call_with_args_and_kwargs():
    assert call(fun, 1, 2, 3, a=1, b=2, c=3) == "hello"

