import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_factory(factory):
    assert factory(fun) is None
    assert factory(fun, 42) is None
    assert factory(fun, 42, 43) is None
    assert factory(fun, 42, 43, 44) is None
    assert factory(fun, 42, 43, 44, 45) is None
    raises(TypeError, factory, fun, 42, 43, 44, 45, 46)

def test_factory_with_args(factory):
    assert factory(fun, 1, 2, 3, 4, 5) is None
    raises(TypeError, factory, fun, 1, 2, 3, 4, 5, 6)

def test_factory_with_kwargs(factory):
    assert factory(fun, a=1, b=2, c=3, d=4, e=5) is None
    raises(TypeError, factory, fun, a=1, b=2, c=3, d=4, e=5, f=6)

def test_factory_with_args_and_kwargs(f
