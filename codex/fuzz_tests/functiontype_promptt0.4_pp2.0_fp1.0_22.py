import types
# Test types.FunctionType
def f(x):
    return x

print(type(f))
print(type(f) == types.FunctionType)

# Test types.MethodType
class A:
    def f(self, x):
        return x

a = A()
print(type(a.f))
print(type(a.f) == types.MethodType)

# Test types.BuiltinFunctionType
print(type(len))
print(type(len) == types.BuiltinFunctionType)

# Test types.BuiltinMethodType
print(type([].append))
print(type([].append) == types.BuiltinMethodType)

# Test types.ModuleType
import math
print(type(math))
print(type(math) == types.ModuleType)

# Test types.TracebackType
try:
    1/0
except:
    import sys
    tb = sys.exc_info()[2]
    print(type(tb))
    print(type(tb) == types.TracebackType)

# Test types.Frame
