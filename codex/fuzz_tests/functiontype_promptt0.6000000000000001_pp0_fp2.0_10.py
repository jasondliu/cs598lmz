import types
# Test types.FunctionType
def func1():
    pass

print(type(func1) == types.FunctionType)

print(type(abs) == types.BuiltinFunctionType)

print(type(lambda x: x) == types.LambdaType)

print(type((x for x in range(10))) == types.GeneratorType)

# Test types.LambdaType

def fn(x, y):
    return x*10 + y

print(fn(1, 2))

L = list(map(fn, [1, 2, 3, 4, 5, 6]))
print(L)

print(list(map(lambda x: x*x, [1, 2, 3, 4, 5, 6])))

# Test types.GeneratorType

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)
print(f)
print(type
