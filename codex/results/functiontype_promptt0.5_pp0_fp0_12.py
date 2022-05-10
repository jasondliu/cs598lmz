import types
# Test types.FunctionType

# __main__
def func(a, b, c=0, d=1, *args, **kwargs):
    pass

print(type(func))

# <class 'function'>
print(type(func) == types.FunctionType)

# False
print(type(func) == types.BuiltinFunctionType)

# True
print(type(abs) == types.BuiltinFunctionType)

# True
print(type(lambda x: x) == types.LambdaType)

# True
print(type((x for x in range(10))) == types.GeneratorType)

# False
print(type(x for x in range(10)) == types.GeneratorType)

# True
print(type(abs) == types.BuiltinFunctionType)

# False
print(type(lambda x: x) == types.BuiltinFunctionType)

# True
print(type((x for x in range(10))) == types.GeneratorType)

# False
print(type(x for x in range(10)) == types.Gener
