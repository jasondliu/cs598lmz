import types
# Test types.FunctionType
def func1():
    pass

print(type(func1))
print(type(abs))
print(type(lambda x: x))
print(type((x for x in range(10))))
print(type(x for x in range(10)))
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

# Test types.LambdaType
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))

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

