import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

def test_fun_with_args():
    @FUNTYPE
    def fun(arg):
        return arg
    assert fun(1) == 1

def test_fun_with_kwargs():
    @FUNTYPE
    def fun(arg, kwarg=None):
        return arg, kwarg
    assert fun(1, kwarg=2) == (1, 2)

def test_fun_with_varargs():
    @FUNTYPE
    def fun(*args):
        return args
    assert fun(1, 2, 3) == (1, 2, 3)

def test_fun_with_varkwargs():
    @FUNTYPE
    def fun(**kwargs):
        return kwargs
    assert fun(a=1, b=2) == {'a': 1, 'b': 2}

def test_fun_with_args_and_kwargs():
    @FUNTYPE
    def fun(*args, **kwargs):
        return
