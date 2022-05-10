import types
# Test types.FunctionType
def test_types_FunctionType():
    def fn(): return 1
    f = types.FunctionType(fn.__code__, fn.__globals__, "foo", fn.__defaults__, fn.__closure__)
    assert f.__name__ == "foo"
    assert f() == 1

# Test types.LambdaType
def test_types_LambdaType():
    l = types.LambdaType(add42.__code__, add42.__globals__, "foo", add42.__defaults__, add42.__closure__)
    assert l.__name__ == "foo"
    assert l(1) == 43

# Test types.CodeType
def test_types_CodeType():
    l = types.LambdaType(add42.__code__, add42.__globals__, "foo", add42.__defaults__, add42.__closure__)
    assert l.__name__ == "foo"
    assert l(1) == 43

# Test types.MappingProxyType

