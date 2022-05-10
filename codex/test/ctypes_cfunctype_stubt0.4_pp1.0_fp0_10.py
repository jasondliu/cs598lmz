import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_call_function():
    assert call_function(fun) == 1

def test_call_function_with_args():
    assert call_function(fun, 1, 2, 3) == 1

def test_call_function_with_kwargs():
    assert call_function(fun, a=1, b=2, c=3) == 1

def test_call_function_with_args_and_kwargs():
    assert call_function(fun, 1, 2, 3, a=1, b=2, c=3) == 1

def test_call_function_with_args_and_kwargs_and_empty_kwargs():
    assert call_function(fun, 1, 2, 3, a=1, b=2, c=3, **{}) == 1

def test_call_function_with_args_and_kwargs_and_empty_args():
    assert call_function(fun, *[], a=1, b=2, c=3) == 1

