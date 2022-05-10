import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

def test_call_py_func():
    assert fun() == "Hello"

def test_call_py_func_with_arg():
    @FUNTYPE
    def fun2(a):
        return a
    assert fun2(42) == 42

def test_call_py_func_with_kwarg():
    @FUNTYPE
    def fun3(a=42):
        return a
    assert fun3(a=43) == 43

def test_call_py_func_with_kwarg_and_default():
    @FUNTYPE
    def fun4(a=42):
        return a
    assert fun4() == 42

def test_call_py_func_with_kwarg_and_default_and_arg():
    @FUNTYPE
    def fun5(a=42, b=43):
        return a+b
    assert fun5(44) == 87

def test_call_py_func_with_kwarg_and_default_and_kwarg():
    @FUNTYPE
    def fun6
