import types
# Test types.FunctionType
assert type(lambda: None) == types.FunctionType

# Test types.LambdaType
assert type(lambda a: None) == types.LambdaType

# Test types.GeneratorType
assert type((lambda: (yield))()) == types.GeneratorType

print('All tests passed!')
