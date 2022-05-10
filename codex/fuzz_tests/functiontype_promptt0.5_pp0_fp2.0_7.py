import types
# Test types.FunctionType
def test_function():
    def f(x):
        return x
    assert type(f) == types.FunctionType

# Test types.ClassType
def test_class():
    class C:
        pass
    assert type(C) == types.ClassType

# Test types.MethodType
def test_method():
    class C:
        def foo(self):
            pass
    assert type(C.foo) == types.MethodType

# Test types.BuiltinFunctionType
def test_builtin_function():
    assert type(len) == types.BuiltinFunctionType
    assert type(id) == types.BuiltinFunctionType
    assert type(hash) == types.BuiltinFunctionType
    assert type(abs) == types.BuiltinFunctionType
    assert type(min) == types.BuiltinFunctionType
    assert type(max) == types.BuiltinFunctionType
    assert type(round) == types.BuiltinFunctionType
    assert type(sum) == types.BuiltinFunctionType

# Test types.BuiltinMethodType
def test_builtin_method
