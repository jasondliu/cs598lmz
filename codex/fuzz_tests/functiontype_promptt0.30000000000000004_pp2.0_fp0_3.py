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

# Test types.BuiltinFunctionType
def test_builtin_function_type():
    assert isinstance(len, types.BuiltinFunctionType)
    assert not isinstance(len, types.FunctionType)
    assert not isinstance(len, types.MethodType)
    assert not isinstance(len, types.BuiltinMethodType)
    assert not isinstance(len, types.LambdaType)

# Test types.MethodType
def test_method_type():
    class C:
        def f(self):
            pass
    c = C()
    assert isinstance(c.f, types.MethodType)
    assert not isinstance(c.f, types.FunctionType)
