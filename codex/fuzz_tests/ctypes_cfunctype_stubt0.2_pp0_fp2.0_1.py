import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_cfunc_call():
    assert fun() == 1

def test_cfunc_call_with_arg():
    assert fun(1) == 1

def test_cfunc_call_with_kwargs():
    assert fun(a=1) == 1

def test_cfunc_call_with_args_and_kwargs():
    assert fun(1, a=1) == 1

def test_cfunc_call_with_kwargs_and_args():
    assert fun(a=1, 1) == 1

def test_cfunc_call_with_args_and_kwargs_and_kwargs():
    assert fun(1, a=1, b=2) == 1

def test_cfunc_call_with_kwargs_and_args_and_kwargs():
    assert fun(a=1, 1, b=2) == 1

def test_cfunc_call_with_kwargs_and_kwargs_and_args():
    assert fun(a=1, b=2, 1) ==
