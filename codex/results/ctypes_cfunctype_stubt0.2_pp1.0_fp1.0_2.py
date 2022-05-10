import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

def test_fun_with_args():
    @FUNTYPE
    def fun(x):
        return x
    assert fun(1) == 1
    assert fun("hello") == "hello"

def test_fun_with_kwargs():
    @FUNTYPE
    def fun(x, y=2):
        return x + y
    assert fun(1) == 3
    assert fun(1, y=3) == 4

def test_fun_with_varargs():
    @FUNTYPE
    def fun(*args):
        return args
    assert fun(1, 2, 3) == (1, 2, 3)

def test_fun_with_varkwargs():
    @FUNTYPE
    def fun(**kwargs):
        return kwargs
    assert fun(x=1, y=2) == {'x': 1, 'y': 2}

def test_fun_with_args_and_kwargs():
    @FUNTYPE
    def fun
