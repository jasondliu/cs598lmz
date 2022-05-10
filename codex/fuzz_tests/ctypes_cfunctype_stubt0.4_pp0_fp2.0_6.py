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

def test_fun_with_kwargs():
    @FUNTYPE
    def fun(arg=42):
        return arg
    assert fun(arg=43) == 43

def test_fun_with_stararg():
    @FUNTYPE
    def fun(*args):
        return args
    assert fun(1, 2, 3) == (1, 2, 3)

def test_fun_with_kwstararg():
    @FUNTYPE
    def fun(**kwargs):
        return kwargs
    assert fun(foo=1, bar=2) == {'foo': 1, 'bar': 2}

def test_fun_with_arg_and_stararg():
    @
