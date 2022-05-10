import types
# Test types.FunctionType and types.LambdaType

def f(x):
    return x

def test_function():
    assert isinstance(f, types.FunctionType)
    assert not isinstance(f, types.LambdaType)

def test_lambda():
    g = lambda x: x
    assert isinstance(g, types.LambdaType)
    assert not isinstance(g, types.FunctionType)

def test_builtin_function():
    assert isinstance(len, types.BuiltinFunctionType)
    assert not isinstance(len, types.FunctionType)
    assert not isinstance(len, types.LambdaType)

def test_builtin_method():
    assert isinstance("".upper, types.BuiltinMethodType)
    assert not isinstance("".upper, types.FunctionType)
    assert not isinstance("".upper, types.LambdaType)

class C(object):
    def foo(self):
        return

def test_method():
    assert isinstance(C.foo, types.MethodType)
    assert not is
