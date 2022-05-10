import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun"

def test_c_function():
    assert fun() == "fun"

def test_c_function_in_class():
    class Foo(object):
        def __init__(self):
            self.fun = fun
    foo = Foo()
    assert foo.fun() == "fun"
