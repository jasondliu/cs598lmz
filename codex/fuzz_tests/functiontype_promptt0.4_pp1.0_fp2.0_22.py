import types
# Test types.FunctionType
def test_function_type():
    def f():
        pass
    assert isinstance(f, types.FunctionType)
    assert not isinstance(f, types.BuiltinFunctionType)
    assert not isinstance(f, types.MethodType)
    assert not isinstance(f, types.BuiltinMethodType)
    assert not isinstance(f, types.LambdaType)
    #
    class X(object):
        def f(self):
            pass
    x = X()
    assert isinstance(x.f, types.MethodType)
    assert not isinstance(x.f, types.FunctionType)
    assert not isinstance(x.f, types.BuiltinFunctionType)
    assert not isinstance(x.f, types.BuiltinMethodType)
    assert not isinstance(x.f, types.LambdaType)
    #
    def f():
        pass
    assert isinstance(f, types.FunctionType)
    assert not isinstance(f, types.BuiltinFunctionType)
    assert not isinstance(f, types.MethodType
