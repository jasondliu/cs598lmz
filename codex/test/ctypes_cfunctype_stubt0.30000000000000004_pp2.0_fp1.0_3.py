import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_py_object_return():
    assert fun() == 42

def test_py_object_return_with_arg():
    assert fun(1) == 42

def test_py_object_return_with_kwarg():
    assert fun(a=1) == 42

def test_py_object_return_with_kwargs():
    assert fun(a=1, b=2) == 42

def test_py_object_return_with_kwargs_and_args():
    assert fun(1, a=1, b=2) == 42

def test_py_object_return_with_kwargs_and_args_and_kwargs():
    assert fun(1, a=1, b=2, c=3) == 42

def test_py_object_return_with_kwargs_and_args_and_kwargs_and_args():
    assert fun(1, 2, a=1, b=2, c=3) == 42

