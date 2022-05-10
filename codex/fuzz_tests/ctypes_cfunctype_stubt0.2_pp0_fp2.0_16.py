import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_fun():
    assert fun() is None

def test_fun_with_arg():
    @FUNTYPE
    def fun(x):
        return x
    assert fun(42) == 42

def test_fun_with_kwarg():
    @FUNTYPE
    def fun(x=42):
        return x
    assert fun() == 42

def test_fun_with_kwargs():
    @FUNTYPE
    def fun(**kwargs):
        return kwargs
    assert fun(x=42) == {'x': 42}

def test_fun_with_stararg():
    @FUNTYPE
    def fun(*args):
        return args
    assert fun(42) == (42,)

def test_fun_with_starstararg():
    @FUNTYPE
    def fun(**kwargs):
        return kwargs
    assert fun(x=42) == {'x': 42}

def test_fun_with_starstararg_and_kwarg():
    @FUNTYPE
    def fun(x
