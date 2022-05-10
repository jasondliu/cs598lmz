import types
# Test types.FunctionType


def test_function_type():
    def func1():
        pass
    myfunc = func1

# Test types.MethodType
    class A(object):
        def func2(self):
            pass
    mymethod = A.func2


# Test types.BuiltinFunctionType
    def test_func3(self):
        pass
    mybuiltin = test_func3

# Test types.BuiltinMethodType
    def test_func4(self):
        pass
    mybuiltinmethod = test_func4.__get__

# Test types.UnboundMethodType
