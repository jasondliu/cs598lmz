import types
# Test types.FunctionType

def test_function_type():
    def f(): pass
    assert isinstance(f, types.FunctionType)
    assert not isinstance(f, types.BuiltinFunctionType)
    assert not isinstance(f, types.MethodType)
    assert not isinstance(f, types.BuiltinMethodType)
    assert not isinstance(f, types.LambdaType)
    assert not isinstance(f, types.UnboundMethodType)

def test_builtin_function_type():
    assert isinstance(len, types.BuiltinFunctionType)
    assert not isinstance(len, types.FunctionType)
    assert not isinstance(len, types.MethodType)
    assert not isinstance(len, types.BuiltinMethodType)
    assert not isinstance(len, types.LambdaType)
    assert not isinstance(len, types.UnboundMethodType)

def test_method_type():
    class A(object):
        def m(self): pass
    assert isinstance(A.m, types.MethodType)
    assert not isinstance(
