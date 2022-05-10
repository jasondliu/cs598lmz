import types
# Test types.FunctionType

def func(x,y):
    return x + y

print(type(func))
print(isinstance(func, types.FunctionType))
print(isinstance(func, types.BuiltinFunctionType))
print(isinstance(func, types.LambdaType))
print(isinstance(func, types.GeneratorType))

print(isinstance(func, object))

# Test types.LambdaType

lamb = lambda x,y: x + y

print(type(lamb))
print(isinstance(lamb, types.FunctionType))
print(isinstance(lamb, types.BuiltinFunctionType))
print(isinstance(lamb, types.LambdaType))
print(isinstance(lamb, types.GeneratorType))

print(isinstance(lamb, object))

# Test types.GeneratorType

def gen(x):
    for i in range(x):
        yield i

print(type(gen))
print(isinstance(gen, types.FunctionType))
print(isinstance(gen, types
