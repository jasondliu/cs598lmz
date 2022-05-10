import types
# Test types.FunctionType
def func(x):
    return x

print(type(func))
print(type(func) == types.FunctionType)

# Test types.LambdaType
lam = lambda x: x
print(type(lam))
print(type(lam) == types.LambdaType)

# Test types.GeneratorType
def gen():
    yield 1

print(type(gen))
print(type(gen()) == types.GeneratorType)

# Test types.BuiltinFunctionType
print(type(abs))
print(type(abs) == types.BuiltinFunctionType)

# Test types.BuiltinMethodType
print(type(str.upper))
print(type(str.upper) == types.BuiltinMethodType)

# Test types.MethodType
class A:
    def method(self):
        pass

print(type(A.method))
print(type(A.method) == types.MethodType)

# Test types.UnboundMethodType
print(type(A.method))
print(type(A.method) == types.
