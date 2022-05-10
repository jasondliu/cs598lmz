import types
# Test types.FunctionType
def foo(): pass
print(type(foo) == types.FunctionType)
print(isinstance(foo, types.FunctionType))

# Test types.LambdaType
bar = lambda: None
print(type(bar) == types.LambdaType)
print(isinstance(bar, types.LambdaType))

# Test types.GeneratorType
def genfoo(): yield 1
print(type(genfoo()) == types.GeneratorType)
print(isinstance(genfoo(), types.GeneratorType))
