import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_py_object_return():
    assert fun() is None

def test_py_object_arg():
    @FUNTYPE
    def fun(x):
        return x
    assert fun(None) is None

def test_py_object_arg_None():
    @FUNTYPE
    def fun(x):
        return x
    assert fun(None) is None

def test_py_object_arg_int():
    @FUNTYPE
    def fun(x):
        return x
    assert fun(42) == 42

def test_py_object_arg_float():
    @FUNTYPE
    def fun(x):
        return x
    assert fun(3.14) == 3.14

def test_py_object_arg_string():
    @FUNTYPE
    def fun(x):
        return x
    assert fun("hello") == "hello"

def test_py_object_arg_unicode():
    @FUNTYPE
    def fun(x):
        return x
