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
    assert call_function(fun, 1, 2, 3, foo=1, bar=2) == 1

def test_call_function_with_args_and_kwargs():
    assert call_function(fun, 1, 2, 3, foo=1, bar=2) == 1

def test_call_function_with_keywords():
    assert call_function(fun, 1, 2, 3, foo=1, bar=2, bar2=3, bar3=4) == 1

def test_call_function_with_keywords_and_args():
    assert call_function(fun, 1, 2, 3, foo=1, bar=2, bar2=3, bar3=4) == 1

def test_call_function_with_kwargs_and_keywords
