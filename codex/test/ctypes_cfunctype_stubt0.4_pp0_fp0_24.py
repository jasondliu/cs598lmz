import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def f():
    return fun()

def g():
    return f()

def h():
    return g()

def test_call_chain():
    assert h() is None

def test_call_chain_with_arg():
    def g(x):
        return x
    def h(x):
        return g(x)
    assert h(42) == 42

def test_call_chain_with_kwargs():
    def g(x, y=0):
        return x + y
    def h(x, y=0):
        return g(x, y=y)
    assert h(1, y=2) == 3

def test_call_chain_with_kwargs_and_kwargs():
    def g(x, y=0):
        return x + y
    def h(x, y=0):
        return g(x, y=y)
    assert h(1, 2) == 3

