import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_fun():
    assert fun() is None

def test_fun_with_args():
    @FUNTYPE
    def fun(a, b):
        return a, b
    assert fun(1, 2) == (1, 2)

def test_fun_with_kwargs():
    @FUNTYPE
    def fun(a, b):
        return a, b
    assert fun(b=2, a=1) == (1, 2)

def test_fun_with_defaults():
    @FUNTYPE
    def fun(a, b=2):
        return a, b
    assert fun(1) == (1, 2)

def test_fun_with_varargs():
    @FUNTYPE
    def fun(a, *args):
        return a, args
    assert fun(1, 2, 3) == (1, (2, 3))

def test_fun_with_varkwargs():
    @FUNTYPE
    def fun(a, **kwargs):
        return a, kwargs
