import types
# Test types.FunctionType
def fun1():
    pass

print(type(fun1) == types.FunctionType)

# Test types.LambdaType
lm = lambda x, y: x + y
print(type(lm) == types.LambdaType)

# Test types.GeneratorType
def fib(n):
    f1, f2, f3 = 0, 1, 1
    while f3 < n:
        yield f3
        f1, f2 = f2, f3
        f3 = f1 + f2

for i in fib(10):
    print(i, end=' ')

print(type(fib))
print(type(fib(10)) == types.GeneratorType)

# Test types.BuiltinFunctionType
print(type(abs) == types.BuiltinFunctionType)

# Test types.BuiltinMethodType
print(type(str.upper) == types.BuiltinMethodType)

# Test types.MethodType
class MyType(type):
    def __init__(cls, *args, **kw
