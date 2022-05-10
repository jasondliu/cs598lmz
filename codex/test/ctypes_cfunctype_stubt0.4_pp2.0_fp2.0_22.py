import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello'

def test_py_object():
    assert fun() == 'hello'
    assert type(fun()) is str

def test_py_object_with_arg():
    @FUNTYPE
    def fun2(arg):
        return arg
    assert fun2(42) == 42
    assert type(fun2(42)) is int

def test_py_object_with_kwarg():
    @FUNTYPE
    def fun3(arg=42):
        return arg
    assert fun3() == 42
    assert fun3(arg=43) == 43

def test_py_object_with_args():
    @FUNTYPE
    def fun4(*args):
        return args
    assert fun4(1, 2, 3) == (1, 2, 3)

def test_py_object_with_kwargs():
    @FUNTYPE
    def fun5(**kwargs):
        return kwargs
    assert fun5(x=1, y=2) == dict(x=1, y=2)

