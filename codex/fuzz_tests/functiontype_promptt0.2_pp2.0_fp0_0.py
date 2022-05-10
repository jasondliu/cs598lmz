import types
# Test types.FunctionType
def func(x):
    return x

print(type(func))
print(type(func) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.LambdaType
f = lambda x: x * x
print(f)
print(f(5))

# Test types.GeneratorType
g = (x * x for x in range(10))
print(g)
for n in g:
    print(n)

# Test types.GeneratorType
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(6)
print('fib(6):', f)
for x in f:
    print(x)

# call generator manually
