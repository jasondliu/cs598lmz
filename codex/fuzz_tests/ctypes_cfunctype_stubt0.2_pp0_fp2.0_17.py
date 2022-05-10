import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

def test_fun_call():
    assert fun.__call__() == "hello"

def test_fun_call_with_args():
    assert fun.__call__(1, 2, 3) == "hello"

def test_fun_call_with_kwargs():
    assert fun.__call__(a=1, b=2, c=3) == "hello"

def test_fun_call_with_args_and_kwargs():
    assert fun.__call__(1, 2, 3, a=1, b=2, c=3) == "hello"

def test_fun_call_with_args_and_kwargs_and_starargs():
    assert fun.__call__(1, 2, 3, a=1, b=2, c=3, *(4, 5, 6)) == "hello"

def test_fun_call_with_args_and_kwargs_and_starargs_and_kwargs():
   
