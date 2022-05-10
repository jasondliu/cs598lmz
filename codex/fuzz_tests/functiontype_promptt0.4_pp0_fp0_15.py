import types
# Test types.FunctionType
def foo():
    pass

print(type(foo))
print(type(foo) == types.FunctionType)
print(type(foo) == types.BuiltinFunctionType)
print(type(foo) == types.LambdaType)
print(type(foo) == types.GeneratorType)
# Test types.LambdaType
g = lambda x: x * x
print(type(g))
print(type(g) == types.FunctionType)
print(type(g) == types.BuiltinFunctionType)
print(type(g) == types.LambdaType)
print(type(g) == types.GeneratorType)
# Test types.GeneratorType
def foo():
    yield 1
    yield 2
    yield 3

g = foo()
print(type(g))
print(type(g) == types.FunctionType)
print(type(g) == types.BuiltinFunctionType)
print(type(g) == types.LambdaType)
print(type(g) == types.GeneratorType)
# Test types.Builtin
