import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello'

def test_fun():
    assert fun() == 'hello'

def test_fun_with_args():
    @FUNTYPE
    def fun(a,b,c):
        return a * b * c
    assert fun(1,2,3) == 6

def test_fun_with_args_and_kwargs():
    @FUNTYPE
    def fun(a,b,c,**kwargs):
        return a * b * c * kwargs['d']
    assert fun(1,2,3,d=4) == 24

def test_fun_with_args_and_kwargs_and_defaults():
    @FUNTYPE
    def fun(a,b=2,c=3,**kwargs):
        return a * b * c * kwargs['d']
    assert fun(1,d=4) == 24

def test_fun_with_args_and_kwargs_and_defaults_and_varargs():
    @FUNTYPE
    def fun(a,b=2,c=3
