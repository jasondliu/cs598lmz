import types
# Test types.FunctionType
def func():
    pass

print(type(func) == types.FunctionType)

# Test types.LambdaType
print(type(lambda: None) == types.LambdaType)

# Test types.GeneratorType
def gen():
    yield 1

g = gen()
print(type(g) == types.GeneratorType)

# Test types.BuiltinFunctionType
print(type(len) == types.BuiltinFunctionType)

# Test types.BuiltinMethodType
print(type([].append) == types.BuiltinMethodType)

# Test types.MethodType
class A:
    def method(self):
        pass

print(type(A.method) == types.MethodType)

# Test types.UnboundMethodType
print(type(A.method) == types.MethodType)

# Test types.ModuleType
import sys
print(type(sys) == types.ModuleType)

# Test types.TracebackType
try:
    raise Exception
except:
    exc_type, exc_value, exc_
