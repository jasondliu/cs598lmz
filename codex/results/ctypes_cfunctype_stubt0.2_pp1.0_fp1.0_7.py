import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_func_type():
    assert fun() == "hello"

def test_func_type_with_args():
    @FUNTYPE
    def fun2(a):
        return a
    assert fun2(42) == 42

def test_func_type_with_kwargs():
    @FUNTYPE
    def fun3(a, b=42):
        return a, b
    assert fun3(1) == (1, 42)
    assert fun3(1, 2) == (1, 2)

def test_func_type_with_starargs():
    @FUNTYPE
    def fun4(a, *args):
        return a, args
    assert fun4(1, 2, 3) == (1, (2, 3))

def test_func_type_with_starstarargs():
    @FUNTYPE
    def fun5(a, **kwargs):
        return a, kwargs
    assert fun5(1, b=2, c=3) == (1, {"b": 2, "c":
