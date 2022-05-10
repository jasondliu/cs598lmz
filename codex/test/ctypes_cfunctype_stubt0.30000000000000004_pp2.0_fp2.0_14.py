import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_basic_function():
    assert fun() == "hello"

def test_function_in_class():
    class A(object):
        @FUNTYPE
        def fun(self):
            return "hello"
    a = A()
    assert a.fun() == "hello"

def test_function_in_class_with_args():
    class A(object):
        @FUNTYPE
        def fun(self, arg):
            return arg
    a = A()
    assert a.fun("hello") == "hello"

def test_function_in_class_with_kwargs():
    class A(object):
        @FUNTYPE
        def fun(self, arg):
            return arg
    a = A()
    assert a.fun(arg="hello") == "hello"

def test_function_in_class_with_args_and_kwargs():
    class A(object):
        @FUNTYPE
        def fun(self, arg):
            return arg
    a = A()
