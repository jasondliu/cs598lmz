import types
# Test types.FunctionType
def test_function_type():
    def f(): pass
    assert type(f) is types.FunctionType

# Test types.BuiltinFunctionType
def test_builtin_function_type():
    assert type(test_function_type) is types.BuiltinFunctionType

# Test types.GeneratorType
def test_generator_type():
    def f(): yield 42
    g = f()
    assert type(g) is types.GeneratorType

# Test types.TypeType
def test_type_type():
    assert type(type(42)) is types.TypeType

# Test types.UnboundMethodType
def test_unbound_method_type():
    assert type(list.append) is types.UnboundMethodType

# Test types.InstanceType
def test_instance_type():
    assert type(list()) is types.InstanceType

# Test types.LambdaType
def test_lambda_type():
    assert type(lambda x: x) is types.LambdaType

# Test types.CodeType
def test_code_type():
