import types
# Test types.FunctionType()
def test_types_FunctionType():
    def function_test():
        pass
    assert isinstance(function_test, types.FunctionType)
    assert not isinstance(lambda x:x, types.FunctionType)

# Test types.MethodType()
def test_types_MethodType():
    class test(object):
        pass
    assert not isinstance(test, types.MethodType)
    assert not isinstance(test(), types.MethodType)
    test.method = lambda self: self
    assert isinstance(test.method, types.MethodType)
    assert isinstance(test().method, types.MethodType)

# Test types.BuiltinFunctionType()
def test_types_BuiltinFunctionType():
    assert isinstance(abs, types.BuiltinFunctionType)
    assert not isinstance(lambda x:x, types.BuiltinFunctionType)

# Test types.BuiltinMethodType()
def test_types_BuiltinMethodType():
    class test(object):
        pass
    assert not isinstance(test, types.BuiltinMethodType)
    assert
