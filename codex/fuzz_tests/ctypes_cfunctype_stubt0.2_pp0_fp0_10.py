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

def test_fun_with_kwarg():
    @FUNTYPE
    def fun(a=1):
        return a
    assert fun(a=2) == 2

def test_fun_with_default_kwarg():
    @FUNTYPE
    def fun(a=1):
        return a
    assert fun() == 1

def test_fun_with_kwargs():
    @FUNTYPE
    def fun(a, b=1, c=2):
        return a, b, c
    assert fun(1, 2, 3) == (1, 2, 3)
    assert fun(1, 2) == (1, 2, 2)
    assert fun(1) == (1, 1, 2)
    assert fun(1, c=3) == (1, 1, 3)

def test_fun_with_args():

