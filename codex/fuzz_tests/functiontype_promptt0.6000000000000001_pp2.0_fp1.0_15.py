import types
# Test types.FunctionType
def f1(a, b):
    return a+b

print(type(f1) == types.FunctionType)

# Test types.LambdaType
f2 = lambda a, b: a+b
print(type(f2) == types.LambdaType)

# Test types.GeneratorType
f3 = (x for x in range(10))
print(type(f3) == types.GeneratorType)

# Test types.MethodType
class A:
    def __init__(self, x):
        self.x = x
    def f(self, a, b):
        return self.x + a + b
a = A(10)
print(type(A.f) == types.FunctionType)
print(type(a.f) == types.MethodType)

# Test types.ModuleType
import math
print(type(math) == types.ModuleType)

# Test types.ClassType
class B:
    def __init__(self, x):
        self.x = x
    def f(self, a
