from types import FunctionType
a = (x for x in [1])
type(a)

def fun(x):
    return x

print(type(fun))
print(type(fun) == FunctionType)
print(type(fun) == type(lambda x: x))

print(type(fun) == types.FunctionType)

print(type(fun) == types.LambdaType)

print(type(lambda x: x))
print(type(lambda x: x) == FunctionType)
print(type(lambda x: x) == types.FunctionType)

print(type(lambda x: x) == types.LambdaType)

print(type(lambda x: x) == type(lambda x: x))
print(type(lambda x: x) == type(lambda x: x))

print(type(lambda x: x) == type(lambda x: x))

print(type(lambda x: x) == type(lambda x: x))

print(type(lambda x: x) == type(lambda x: x))

print(type(lambda x: x) == type(lambda x: x))


