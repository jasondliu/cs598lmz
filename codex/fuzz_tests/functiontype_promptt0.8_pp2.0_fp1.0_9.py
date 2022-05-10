import types
# Test types.FunctionType

def f(x):
    return x

a = types.FunctionType(f.__code__, f.__globals__)

print(a is f)
print(a(3) == f(3))

print(type(a.__globals__))


d = {'a': 'abc'}

def f(x):
    return d['a']

a = types.FunctionType(f.__code__, f.__globals__)

print (a is f)


print(a(42))

d['a'] = 'def'

print(a(42))

print(type(a.__globals__))


# Test types.LambdaType

a = types.LambdaType(lambda: 3)

print(a())
