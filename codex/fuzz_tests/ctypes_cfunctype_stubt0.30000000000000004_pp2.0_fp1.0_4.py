import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_fun():
    assert fun() is None

def test_fun_return_none():
    assert fun() is None

def test_fun_return_none_with_arg(arg):
    assert fun() is None

def test_fun_return_none_with_kwarg(arg=None):
    assert fun() is None

def test_fun_return_none_with_arg_and_kwarg(arg, kwarg=None):
    assert fun() is None

def test_fun_return_none_with_arg_and_varargs(*args):
    assert fun() is None

def test_fun_return_none_with_arg_and_varargs_and_kwargs(arg, *args, **kwargs):
    assert fun() is None

def test_fun_return_none_with_varargs(*args):
    assert fun() is None

def test_fun_return_none_with_varargs_and_kwargs(*args, **kwargs):
    assert fun() is None

def test_
