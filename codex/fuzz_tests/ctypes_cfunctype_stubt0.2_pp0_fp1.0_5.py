import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_fun():
    assert fun() is None

def test_fun_with_arg():
    @FUNTYPE
    def fun(arg):
        return arg
    assert fun(42) == 42

def test_fun_with_args():
    @FUNTYPE
    def fun(arg1, arg2):
        return arg1, arg2
    assert fun(42, 43) == (42, 43)

def test_fun_with_kwargs():
    @FUNTYPE
    def fun(arg1, arg2):
        return arg1, arg2
    assert fun(arg2=43, arg1=42) == (42, 43)

def test_fun_with_defaults():
    @FUNTYPE
    def fun(arg1, arg2=42):
        return arg1, arg2
    assert fun(43) == (43, 42)

def test_fun_with_varargs():
    @FUNTYPE
    def fun(*args):
        return args
    assert fun(1, 2, 3) == (1, 2
