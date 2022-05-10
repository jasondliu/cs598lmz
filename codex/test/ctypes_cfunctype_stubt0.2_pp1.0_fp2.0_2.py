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
    assert fun(42) == 42

def test_fun_with_kwarg():
    @FUNTYPE
    def fun(arg=42):
        return arg
    assert fun() == 42

def test_fun_with_args():
    @FUNTYPE
    def fun(a, b, c):
        return a, b, c
    assert fun(1, 2, 3) == (1, 2, 3)

def test_fun_with_kwargs():
    @FUNTYPE
    def fun(a=1, b=2, c=3):
        return a, b, c
    assert fun() == (1, 2, 3)
    assert fun(4, 5, 6) == (4, 5, 6)
    assert fun(4, 5) == (4, 5, 3)
    assert fun(4) == (4, 2, 3)
