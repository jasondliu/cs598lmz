import types
# Test types.FunctionType
def func(a, b, c):
    return a + b + c

print(type(func))
print(type(func) is types.FunctionType)
print(type(func) is types.BuiltinFunctionType)

# Test types.GeneratorType
def generator(n):
    for i in range(n):
        yield i

print(type(generator))
print(type(generator) is types.GeneratorType)
print(type(generator(10)) is types.GeneratorType)

# Test types.LambdaType
print(type(lambda x: x) is types.LambdaType)
print(type(lambda x: x * 2) is types.LambdaType)
print(type(lambda x: x ** 2) is types.LambdaType)

# Test types.MethodType
class A:
    def __init__(self, a):
        self.a = a

    def method(self, b):
        return self.a + b

a = A(10)
print(type(a.method))
