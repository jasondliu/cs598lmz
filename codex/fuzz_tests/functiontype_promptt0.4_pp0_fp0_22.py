import types
# Test types.FunctionType
def test_function_type():
    def f(): pass
    assert isinstance(f, types.FunctionType)
    assert not isinstance(f, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
def test_builtin_function_type():
    assert isinstance(len, types.BuiltinFunctionType)
    assert not isinstance(len, types.FunctionType)

# Test types.LambdaType
def test_lambda_type():
    f = lambda: None
    assert isinstance(f, types.LambdaType)
    assert not isinstance(f, types.FunctionType)
    assert not isinstance(f, types.BuiltinFunctionType)

# Test types.GeneratorType
def test_generator_type():
    def f(): yield
    assert isinstance(f(), types.GeneratorType)
    assert not isinstance(f, types.FunctionType)
    assert not isinstance(f, types.BuiltinFunctionType)

# Test types.CodeType
def test_code_type():
    def f(): pass
   
