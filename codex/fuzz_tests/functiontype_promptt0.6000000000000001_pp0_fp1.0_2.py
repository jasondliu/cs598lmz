import types
# Test types.FunctionType
def functest(x):
    return x + 42

# Test types.LambdaType
lambdatest = lambda x: x + 42

# Test types.GeneratorType
def gentest(n):
    i = 0
    while i < n:
        yield i
        i += 1

print(isinstance(functest, types.FunctionType))
print(isinstance(lambdatest, types.LambdaType))
print(isinstance(gentest(10), types.GeneratorType))

# Test types.BuiltinFunctionType
print(isinstance(len, types.BuiltinFunctionType))

# Test types.BuiltinMethodType
print(isinstance([].append, types.BuiltinMethodType))

# Test types.MethodType
class C:
    def method(self): pass
c = C()
print(isinstance(c.method, types.MethodType))

# Test types.ModuleType
import sys
print(isinstance(sys, types.ModuleType))

# Test types.TracebackType
try:
    raise
