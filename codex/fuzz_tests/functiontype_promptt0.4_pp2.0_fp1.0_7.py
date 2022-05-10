import types
# Test types.FunctionType
def f(): pass
assert type(f) == types.FunctionType
assert type(f) != types.BuiltinFunctionType
assert type(f) != types.BuiltinMethodType
assert type(f) != types.MethodType
assert type(f) != types.LambdaType
assert type(f) != types.GeneratorType
# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
assert type(len) != types.FunctionType
assert type(len) != types.BuiltinMethodType
assert type(len) != types.MethodType
assert type(len) != types.LambdaType
assert type(len) != types.GeneratorType
# Test types.BuiltinMethodType
assert type([].append) == types.BuiltinMethodType
assert type([].append) != types.FunctionType
assert type([].append) != types.BuiltinFunctionType
assert type([].append) != types.MethodType
assert type([].append) != types.LambdaType
assert type([].append) != types.GeneratorType
# Test types.MethodType
