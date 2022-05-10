import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ("Hello", "World")

def test_return_tuple():
    assert _call(fun) == ("Hello", "World")

def test_invoke_tuple():
    _call(_invoker(fun), 1, 2, 3)
    _call(_invoker(fun), 1, 2, 3, 4, 5)
    _call(_invoker(fun), 1, 2, 3, 4, 5, 6, 7)
    _call(_invoker(fun), 1, 2, 3, 4, 5, 6, 7, 8, 9)
    _call(_invoker(fun), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
    _call(_invoker(fun), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    _call(_invoker(fun), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
