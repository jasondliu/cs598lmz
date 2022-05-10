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
L = lambda x: x * x
print(type(L))
print(type(L) == types.LambdaType)

# Test types.GeneratorType
L = (x for x in range(10))
print(type(L))
print(type(L) == types.GeneratorType)

# Test types.BuiltinFunctionType
import builtins
print(type(abs) == types.BuiltinFunctionType)
print(type(builtins.abs) == types.BuiltinFunctionType)

# Test types.MethodType
class A:
    def __init__(self, x):
        self.x = x
    def method(self, x):
       
