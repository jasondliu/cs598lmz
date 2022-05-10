import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_call_function():
    assert call_function(fun) == 1

def test_call_function_with_arg():
    assert call_function(fun, 1) == 1

def test_call_function_with_kwargs():
    assert call_function(fun, x=1) == 1

def test_call_function_with_arg_and_kwargs():
    assert call_function(fun, 1, x=1) == 1

def test_call_function_with_args():
    assert call_function(fun, 1, 2) == 1

def test_call_function_with_args_and_kwargs():
    assert call_function(fun, 1, 2, x=1) == 1

def test_call_function_with_kwargs_and_kwargs():
    assert call_function(fun, x=1, y=2) == 1

