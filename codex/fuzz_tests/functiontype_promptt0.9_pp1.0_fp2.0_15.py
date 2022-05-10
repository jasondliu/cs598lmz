import types
# Test types.FunctionType and types.LambdaType
def func(*params): pass

assert type(func) == types.FunctionType

lambda_func = lambda *params: None

assert type(lambda_func) == types.LambdaType
# Test types.BuiltinType (includes classes)
instance = object()

assert type(instance) == types.BuiltinFunctionType
assert type(lambda_func) == types.BuiltinFunctionType

# Note that some built-in functions (eg. methods) will show as
# built-in type = FunctionType

assert type(object) == types.BuiltinFunctionType
# type is also a built-in method, but it will show up as a FunctionType

assert type(type) == types.BuiltinFunctionType
# This is to show that type(type) shows up as a FunctionType, not a
# BuiltinType Function.

assert type(type) == types.FunctionType
# Test types.ObjectType
instance = object()

assert type(instance) == types.ObjectType

# Test completed successfully
print("All tests completed successfully!")
