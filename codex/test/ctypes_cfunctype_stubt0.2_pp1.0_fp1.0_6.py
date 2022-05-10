import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_fun():
    assert fun() == 1

def test_fun_with_args():
    @FUNTYPE
    def fun(a, b):
        return a + b
    assert fun(1, 2) == 3

def test_fun_with_kwargs():
    @FUNTYPE
    def fun(a, b):
        return a + b
    assert fun(a=1, b=2) == 3

def test_fun_with_args_and_kwargs():
    @FUNTYPE
    def fun(a, b):
        return a + b
    assert fun(1, b=2) == 3

def test_fun_with_defaults():
    @FUNTYPE
    def fun(a, b=1):
        return a + b
    assert fun(1) == 2
    assert fun(1, 2) == 3

def test_fun_with_defaults_and_kwargs():
    @FUNTYPE
    def fun(a, b=1):
        return a + b
