import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_fun():
    assert fun() is None

def test_fun_with_args():
    @FUNTYPE
    def fun(a):
        return a
    assert fun(1) == 1

def test_fun_with_kwargs():
    @FUNTYPE
    def fun(a, b=1):
        return a, b
    assert fun(1) == (1, 1)
    assert fun(1, 2) == (1, 2)

def test_fun_with_varargs():
    @FUNTYPE
    def fun(*args):
        return args
    assert fun(1, 2, 3) == (1, 2, 3)

def test_fun_with_kwargs_and_varargs():
    @FUNTYPE
    def fun(*args, **kwargs):
        return args, kwargs
    assert fun(1, 2, 3, a=4, b=5) == ((1, 2, 3), {'a': 4, 'b': 5})

def test_fun_with_defaults():
   
