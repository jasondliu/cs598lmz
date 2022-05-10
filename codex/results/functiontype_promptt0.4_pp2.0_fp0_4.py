import types
# Test types.FunctionType
def func(a, b, c):
    return a + b + c

print(func(1, 2, 3))
print(type(func))
print(isinstance(func, types.FunctionType))

# Test types.LambdaType
lamb = lambda x: x**2
print(lamb(2))
print(type(lamb))
print(isinstance(lamb, types.LambdaType))

# Test types.GeneratorType
def gen(n):
    for i in range(n):
        yield i

g = gen(5)
print(type(g))
print(isinstance(g, types.GeneratorType))

# Test types.BuiltinFunctionType
print(type(abs))
print(isinstance(abs, types.BuiltinFunctionType))

# Test types.BuiltinMethodType
print(type(str.upper))
print(isinstance(str.upper, types.BuiltinMethodType))

# Test types.MethodType
class Foo:
    def bar(self):
        pass

f = Foo()
