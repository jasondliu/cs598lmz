import types
# Test types.FunctionType
def test_function_type():
  assert isinstance(test_function_type, types.FunctionType)

# Test types.LambdaType
test_lambda_type = lambda x: x

assert isinstance(test_lambda_type, types.LambdaType)

# Test types.GeneratorType
def test_generator_type_gen():
  yield 1

assert isinstance(test_generator_type_gen(), types.GeneratorType)

# Test types.GeneratorType
test_generator_type_gen_expr = (x for x in [1, 2, 3])
assert isinstance(test_generator_type_gen_expr, types.GeneratorType)

# Test types.BuiltinMethodType
assert isinstance(test_generator_type_gen_expr.next, types.BuiltinMethodType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.MethodType
assert isinstance(str.lower, types.MethodType)

# Test types.UnboundMethod
