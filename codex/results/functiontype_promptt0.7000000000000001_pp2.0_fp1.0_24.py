import types
# Test types.FunctionType
def function(x):
    return x * x

print(type(function) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test isinstance()
print(isinstance(function, types.FunctionType))
print(isinstance(abs, types.BuiltinFunctionType))
print(isinstance(lambda x: x, types.FunctionType))
print(isinstance((x for x in range(10)), types.GeneratorType))

# Test dir()
print(dir(types))

# type()
print(type(123))
print(type(abs))
print(type('str'))
print(type(None))
print(type(123) == type(456))
print(type(123) == int)
print(type('abc') == type('123'))
print(type('abc') == str)
print(type('abc') == type(123))

