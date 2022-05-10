import types
# Test types.FunctionType
assert(types.FunctionType == type(function_type))
assert(types.FunctionType == type(FunctionType))

# Test types.LambdaType
assert(types.LambdaType == type(lambda_type))
assert(types.LambdaType == type(LambdaType))

# Test types.MethodType
assert(types.MethodType == type(method_type))
assert(types.MethodType == type(MethodType))

# Test types.BuiltinFunctionType
assert(types.BuiltinFunctionType == type(builtin_function_type))
assert(types.BuiltinFunctionType == type(BuiltinFunctionType))

# Test types.BuiltinMethodType
assert(types.BuiltinMethodType == type(builtin_method_type))
assert(types.BuiltinMethodType == type(BuiltinMethodType))

# Test types.GeneratorType
assert(types.GeneratorType == type(generator_type))
assert(types.GeneratorType == type(GeneratorType))

# Test types.ModuleType
assert(types.ModuleType == type(
