import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"

def test_call():
    assert fun() == "hello world"

def test_call_with_arg():
    assert fun(1) == "hello world"

def test_call_with_kwargs():
    assert fun(a=1) == "hello world"

def test_call_with_args_and_kwargs():
    assert fun(1, a=1) == "hello world"
