import types
# Test types.FunctionType

def f():
    pass

assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(print, types.BuiltinFunctionType)
assert isinstance(len, types.BuiltinFunctionType)
assert isinstance(min, types.BuiltinFunctionType)
assert isinstance(max, types.BuiltinFunctionType)
assert isinstance(sum, types.BuiltinFunctionType)

# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)

# Test types.GeneratorType
assert isinstance((i for i in range(10)), types.GeneratorType)

# Test types.GeneratorType
assert isinstance(iter((i for i in range(10))), types.GeneratorType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
assert isinstance((lambda: None).__code__, types.CodeType)
assert isinstance((i for i in range(10)).__code__, types.CodeType)

# Test types
