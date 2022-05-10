import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_fun():
    assert fun() is None

def test_fun_with_arg():
    @FUNTYPE
    def fun(arg):
        return arg
    assert fun(1) == 1

def test_fun_with_kwarg():
    @FUNTYPE
    def fun(arg=1):
        return arg
    assert fun() == 1

def test_fun_with_args():
    @FUNTYPE
    def fun(*args):
        return args
    assert fun(1, 2, 3) == (1, 2, 3)

def test_fun_with_kwargs():
    @FUNTYPE
    def fun(**kwargs):
        return kwargs
    assert fun(a=1, b=2, c=3) == {'a': 1, 'b': 2, 'c': 3}

def test_fun_with_args_and_kwargs():
    @FUNTYPE
    def fun(*args, **kwargs):
        return args, kwargs
