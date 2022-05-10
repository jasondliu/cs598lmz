import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_fun():
    assert fun() == 1

def test_fun_with_arg():
    @FUNTYPE
    def fun(a):
        return a
    assert fun(1) == 1

def test_fun_with_args():
    @FUNTYPE
    def fun(a, b):
        return a + b
    assert fun(1, 2) == 3

def test_fun_with_kwargs():
    @FUNTYPE
    def fun(a, b=1):
        return a + b
    assert fun(1, b=2) == 3

def test_fun_with_kwargs_and_defaults():
    @FUNTYPE
    def fun(a, b=1, c=2):
        return a + b + c
    assert fun(1, b=2, c=3) == 6

def test_fun_with_kwargs_and_defaults_and_args():
    @FUNTYPE
    def fun(a, b=1, c=2):
        return a + b + c
   
