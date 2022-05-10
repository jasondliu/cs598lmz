import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_fun():
    assert fun() == 42

def test_fun_with_arg():
    @FUNTYPE
    def fun(x):
        return x+1
    assert fun(41) == 42

def test_fun_with_kwarg():
    @FUNTYPE
    def fun(x=41):
        return x+1
    assert fun() == 42

def test_fun_with_kwargs():
    @FUNTYPE
    def fun(**kwds):
        return kwds['x']+1
    assert fun(x=41) == 42

def test_fun_with_args():
    @FUNTYPE
    def fun(*args):
        return args[0]+1
    assert fun(41) == 42

def test_fun_with_args_and_kwargs():
    @FUNTYPE
    def fun(*args, **kwds):
        return args[0]+kwds['x']
    assert fun(41, x=1) == 42

