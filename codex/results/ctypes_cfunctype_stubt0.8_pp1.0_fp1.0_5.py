import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_function_type():
    f = function(fun, types.intp)
    assert f() == 1

def test_function_type_with_class():
    class MyClass(object):
        def __init__(self, v):
            self.v = v
    f = function(fun, types.intp)
    assert f() == 1

def test_function_type_with_kwds():
    @jit(nopython=True)
    def foo(a, b=2):
        return a + b

    assert foo(1) == 3
    assert foo(1, b=3) == 4

def test_function_type_with_kwds_default_none():
    @jit(nopython=True)
    def foo(a, b=None):
        if b is None:
            b = 2
        return a + b

    assert foo(1) == 3
    assert foo(1, b=3) == 4

def test_function_type_with_varargs():
    @jit(n
