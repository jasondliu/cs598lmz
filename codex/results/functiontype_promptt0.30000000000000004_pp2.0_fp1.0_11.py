import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType
assert type(f) == types.BuiltinFunctionType
assert type(f) == types.BuiltinMethodType
assert type(lambda x: x) == types.LambdaType
assert type(lambda x: x) == types.FunctionType
assert type(lambda x: x) == types.BuiltinFunctionType
assert type(lambda x: x) == types.BuiltinMethodType
assert type(lambda x: x).__name__ == 'function'
assert type(lambda x: x).__name__ == 'builtin_function_or_method'
assert type(lambda x: x).__name__ == 'builtin_function_or_method'
assert type(lambda x: x).__name__ == 'function'
assert type(lambda x: x).__name__ == 'function'
assert type(lambda x: x).__name__ == 'function'
assert type(lambda x: x).__name__ == 'function'
assert type(lambda x: x).__name__ == 'function'
assert type(lambda x:
