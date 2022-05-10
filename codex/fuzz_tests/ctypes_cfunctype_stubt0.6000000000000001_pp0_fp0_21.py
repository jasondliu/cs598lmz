import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_py_call_py():
    assert fun() == 42
    assert py_call_py(fun) == 42
    assert py_call_py(fun, 42) == 42
    assert py_call_py(fun, 42, 42) == 42
    assert py_call_py(fun, 42, 42, 42) == 42

def test_py_call_py_with_exception():
    def g(x):
        if x:
            raise ValueError(x)
        return x
    py_call_py(g, 1)

def test_py_call_py_with_exception_2():
    def g(x):
        if x:
            raise ValueError(x)
        return x
    py_call_py(g, 1, 2)

def test_py_call_py_with_exception_3():
    def g(x):
        if x:
            raise ValueError(x)
        return x
    py_call_py(g, 1, 2, 3)

def test
