import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_function_type():
    assert fun() == "hello"

def test_function_type_with_args():
    @FUNTYPE
    def fun2(a):
        return a
    assert fun2(1) == 1

def test_function_type_with_kwargs():
    @FUNTYPE
    def fun3(a, b=1):
        return a + b
    assert fun3(1) == 2
    assert fun3(1, b=2) == 3

def test_function_type_with_starargs():
    @FUNTYPE
    def fun4(a, *args):
        return a + len(args)
    assert fun4(1, 2, 3) == 4

def test_function_type_with_starstarargs():
    @FUNTYPE
    def fun5(a, **kwargs):
        return a + len(kwargs)
    assert fun5(1, b=2, c=3) == 3

