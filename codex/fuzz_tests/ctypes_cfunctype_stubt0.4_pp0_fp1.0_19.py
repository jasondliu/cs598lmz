import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello World"

def test_function_type():
    assert fun() == "Hello World"

def test_function_type_as_argument():
    @FUNTYPE
    def fun2(f):
        return f()
    assert fun2(fun) == "Hello World"

def test_function_type_as_return_type():
    @FUNTYPE
    def fun3():
        return fun
    assert fun3()() == "Hello World"

def test_function_type_as_argument_and_return_type():
    @FUNTYPE
    def fun4(f):
        return f
    assert fun4(fun)() == "Hello World"

def test_function_type_as_argument_and_return_type_2():
    @FUNTYPE
    def fun5(f):
        return f
    assert fun5(fun5(fun))() == "Hello World"


def test_function_type_as_return_type_2():
    @FUNTYPE
    def fun6():
        return fun6
    assert fun6()
