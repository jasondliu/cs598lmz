import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_fun():
    assert fun() == 1

def test_fun_with_arguments():
    @FUNTYPE
    def fun(a, b):
        return a + b
    assert fun(1, 2) == 3

def test_fun_with_defaults():
    @FUNTYPE
    def fun(a, b=2):
        return a + b
    assert fun(1) == 3
    assert fun(1, 2) == 3

def test_fun_with_keywords():
    @FUNTYPE
    def fun(a, b=2):
        return a + b
    assert fun(1, b=2) == 3

def test_fun_with_varargs():
    @FUNTYPE
    def fun(*args):
        return args
    assert fun(1, 2, 3) == (1, 2, 3)

def test_fun_with_varargs_and_keywords():
    @FUNTYPE
    def fun(*args, **kwds):
        return args, kwds
    assert fun(1
