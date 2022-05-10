import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_call():
    assert fun() == 1

def test_call_with_args():
    assert fun(1, 2, 3) == 1

def test_call_with_kwargs():
    assert fun(a=1, b=2, c=3) == 1

def test_call_with_args_and_kwargs():
    assert fun(1, 2, 3, a=1, b=2, c=3) == 1

def test_call_with_args_and_kwargs():
    assert fun(1, 2, 3, a=1, b=2, c=3) == 1

def test_call_with_args_and_kwargs():
    assert fun(1, 2, 3, a=1, b=2, c=3) == 1

def test_call_with_args_and_kwargs():
    assert fun(1, 2, 3, a=1, b=2, c=3) == 1

def test_call_with_args_and_kwargs():
    assert
