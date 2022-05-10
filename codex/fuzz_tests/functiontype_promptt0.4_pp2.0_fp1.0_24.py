import types
# Test types.FunctionType
def func(x):
    return x

print(type(func) is types.FunctionType)
print(type(lambda x: x) is types.LambdaType)
print(type((x for x in range(10))) is types.GeneratorType)

# Test types.MethodType
class A:
    def method(self):
        pass

print(type(A.method) is types.MethodType)
a = A()
print(type(a.method) is types.MethodType)

# Test types.BuiltinFunctionType
print(type(len) is types.BuiltinFunctionType)
print(type(iter) is types.BuiltinFunctionType)

# Test types.BuiltinMethodType
print(type([].append) is types.BuiltinMethodType)
print(type({}.get) is types.BuiltinMethodType)

# Test types.ModuleType
import sys
print(type(sys) is types.ModuleType)

# Test types.TracebackType
try:
    raise Exception()
except:
    exc_type, exc_
