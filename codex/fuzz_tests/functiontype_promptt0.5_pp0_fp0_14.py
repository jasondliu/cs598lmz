import types
# Test types.FunctionType
def func(x):
    return x

print(func(1))
print(type(func))
print(type(func) == types.FunctionType)
print(isinstance(func, types.FunctionType))

# Test types.LambdaType
lambd = lambda x: x
print(lambd(1))
print(type(lambd))
print(type(lambd) == types.LambdaType)
print(isinstance(lambd, types.LambdaType))

# Test types.GeneratorType
gen = (x for x in range(5))
print(next(gen))
print(type(gen))
print(type(gen) == types.GeneratorType)
print(isinstance(gen, types.GeneratorType))

# Test types.CodeType
code = func.__code__
print(code.co_code)
print(type(code))
print(type(code) == types.CodeType)
print(isinstance(code, types.CodeType))
