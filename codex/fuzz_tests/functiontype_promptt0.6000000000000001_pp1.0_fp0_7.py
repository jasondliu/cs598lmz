import types
# Test types.FunctionType
def foo():
    pass

print(foo)
print(type(foo))
print(type(foo) == types.FunctionType)

# Test types.LambdaType
bar = lambda: None
print(bar)
print(type(bar))
print(type(bar) == types.LambdaType)

# Test types.GeneratorType
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fib()
print(fib_gen)
print(type(fib_gen))
print(type(fib_gen) == types.GeneratorType)
