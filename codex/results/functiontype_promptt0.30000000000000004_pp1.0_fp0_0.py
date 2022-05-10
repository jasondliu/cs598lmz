import types
# Test types.FunctionType
def func(a, b):
    return a + b

print(type(func))
print(type(func) is types.FunctionType)

# Test types.LambdaType
l = lambda x, y: x + y
print(type(l))
print(type(l) is types.LambdaType)

# Test types.GeneratorType
def gen():
    yield 1
    yield 2

g = gen()
print(type(g))
print(type(g) is types.GeneratorType)

# Test types.MethodType
class A(object):
    def method(self):
        pass

a = A()
print(type(a.method))
print(type(a.method) is types.MethodType)

# Test types.BuiltinMethodType
print(type(list.append))
print(type(list.append) is types.BuiltinMethodType)

# Test types.BuiltinFunctionType
print(type(len))
print(type(len) is types.BuiltinFunctionType)

# Test types.Module
