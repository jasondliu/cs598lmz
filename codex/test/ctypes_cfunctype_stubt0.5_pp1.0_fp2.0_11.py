import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_fun():
    assert fun() == 1

def test_make_function():
    def f():
        return 1
    assert make_function(f, [], None, None, None)() == 1
    assert make_function(f, [], None, None, None).__name__ == f.__name__

def test_make_function_docstring():
    def f():
        "hello world"
        return 1
    assert make_function(f, [], None, None, None).__doc__ == "hello world"

def test_make_function_defaults():
    def f(x, y=1):
        return x + y
    f2 = make_function(f, [types.intp, types.intp], None, (1,), None)
    assert f2(3) == 4
    f3 = make_function(f, [types.intp, types.intp], None, (2,), None)
    assert f3(3) == 5

