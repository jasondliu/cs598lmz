import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_fun():
    assert fun() == 1

def test_fun_with_args():
    @FUNTYPE
    def fun(x):
        return x+1
    assert fun(1) == 2

def test_fun_with_kwargs():
    @FUNTYPE
    def fun(x=1):
        return x+1
    assert fun(x=1) == 2

def test_fun_with_args_and_kwargs():
    @FUNTYPE
    def fun(x, y=1):
        return x+y
    assert fun(1, y=2) == 3

def test_fun_with_starargs():
    @FUNTYPE
    def fun(*args):
        return args
    assert fun(1, 2, 3) == (1, 2, 3)

def test_fun_with_starargs_and_kwargs():
    @FUNTYPE
    def fun(*args, **kwargs):
        return args, kwargs
