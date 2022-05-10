import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_call_function():
    assert fun() == "hello"

def test_call_function_with_arguments():
    def f(x):
        return x + 1
    f = FUNTYPE(f)
    assert f(1) == 2

def test_call_function_with_keyword_arguments():
    def f(x, y=1):
        return x + y
    f = FUNTYPE(f)
    assert f(1) == 2
    assert f(1, y=2) == 3

def test_call_function_with_star_arguments():
    def f(x, *args):
        return x + len(args)
    f = FUNTYPE(f)
    assert f(1) == 1
    assert f(1, 2) == 2
    assert f(1, 2, 3) == 3

def test_call_function_with_starstar_arguments():
    def f(x, **kwds):
        return x + len(kwds)
    f = FUNTYPE(
