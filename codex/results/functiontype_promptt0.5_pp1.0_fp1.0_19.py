import types
# Test types.FunctionType
def test_types_function_type():
    def foo():
        pass
    foo_type = types.FunctionType(foo.__code__, foo.__globals__, foo.__name__, foo.__defaults__, foo.__closure__)
    assert isinstance(foo_type, types.FunctionType)

# Test types.MethodType
def test_types_method_type():
    class C:
        def foo(self):
            pass
    c = C()
    c_method = types.MethodType(c.foo, c)
    assert isinstance(c_method, types.MethodType)

# Test types.BuiltinFunctionType
def test_types_builtin_function_type():
    def foo():
        pass
    foo_type = types.BuiltinFunctionType(foo.__code__, foo.__globals__, foo.__name__, foo.__defaults__, foo.__closure__)
    assert isinstance(foo_type, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
def test
