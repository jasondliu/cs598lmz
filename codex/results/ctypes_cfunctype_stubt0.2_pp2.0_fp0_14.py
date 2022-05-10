import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_fun():
    assert fun() == 1

def test_fun_callable():
    assert callable(fun)

def test_fun_call():
    assert fun() == 1

def test_fun_call_args():
    assert fun(1) == 1

def test_fun_call_kwargs():
    assert fun(a=1) == 1

def test_fun_call_args_kwargs():
    assert fun(1, a=1) == 1

def test_fun_call_args_kwargs_args():
    assert fun(1, a=1, 2) == 1

def test_fun_call_args_kwargs_args_kwargs():
    assert fun(1, a=1, 2, b=2) == 1

def test_fun_call_args_kwargs_args_kwargs_args():
    assert fun(1, a=1, 2, b=2, 3) == 1

def test_fun_call_args_kwargs_args_kwargs_args_kwargs
