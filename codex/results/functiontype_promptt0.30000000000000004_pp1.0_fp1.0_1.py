import types
# Test types.FunctionType
def test_function_type():
    def f():
        pass
    assert isinstance(f, types.FunctionType)

# Test types.LambdaType
def test_lambda_type():
    f = lambda: None
    assert isinstance(f, types.LambdaType)

# Test types.GeneratorType
def test_generator_type():
    def f():
        yield
    g = f()
    assert isinstance(g, types.GeneratorType)

# Test types.CodeType
def test_code_type():
    def f():
        pass
    assert isinstance(f.__code__, types.CodeType)

# Test types.BuiltinFunctionType
def test_builtin_function_type():
    assert isinstance(len, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
def test_builtin_method_type():
    assert isinstance(''.__len__, types.BuiltinMethodType)

# Test types.MethodType
def test_method_type():
    class C:
        def
