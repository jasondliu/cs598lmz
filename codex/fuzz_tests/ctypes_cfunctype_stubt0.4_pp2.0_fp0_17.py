import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_function():
    assert fun() == "hello"

def test_function_call():
    assert Function(fun)() == "hello"

def test_function_call_with_args():
    @FUNTYPE
    def fun2(a, b):
        return a + b
    assert Function(fun2)(1, 2) == 3

def test_function_call_with_kwargs():
    @FUNTYPE
    def fun3(a, b):
        return a + b
    assert Function(fun3)(b=1, a=2) == 3

def test_function_call_with_args_and_kwargs():
    @FUNTYPE
    def fun4(a, b):
        return a + b
    assert Function(fun4)(1, b=2) == 3

def test_function_call_with_args_and_kwargs_2():
    @FUNTYPE
    def fun5(a, b):
        return a + b
    assert Function(fun5)(b=2, a=1)
