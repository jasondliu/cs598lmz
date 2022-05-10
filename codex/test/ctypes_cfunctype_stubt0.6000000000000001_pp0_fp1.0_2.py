import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 6
def fun2(a):
    return a

def test_function_returns_function():
    class X(object):
        def f(self):
            return fun
    class Y(object):
        def f(self):
            return fun2
    x = X()
    y = Y()
    assert x.f()() == 6
    assert y.f()(7) == 7

def test_function_returns_function_in_op_call():
    class X(object):
        def __call__(self):
            return fun
    class Y(object):
        def __call__(self):
            return fun2
    x = X()
    y = Y()
    assert x()() == 6
    assert y()(7) == 7

def test_function_returns_function_in_method_call():
    class X(object):
        def __call__(self):
            return fun
    class Y(object):
        def __call__(self):
            return fun2
