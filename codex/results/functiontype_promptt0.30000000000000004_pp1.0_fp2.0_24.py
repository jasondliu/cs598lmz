import types
# Test types.FunctionType
def func():
    pass

print(type(func) == types.FunctionType)

# Test types.LambdaType
lam = lambda: None
print(type(lam) == types.LambdaType)

# Test types.GeneratorType
def gen():
    yield 1

g = gen()
print(type(g) == types.GeneratorType)

# Test types.BuiltinFunctionType
print(type(abs) == types.BuiltinFunctionType)

# Test types.BuiltinMethodType
print(type([].append) == types.BuiltinMethodType)

# Test types.MethodType
class C:
    def method(self):
        pass

print(type(C.method) == types.MethodType)

# Test types.UnboundMethodType
print(type(C.method) == types.UnboundMethodType)

# Test types.ModuleType
import sys
print(type(sys) == types.ModuleType)

# Test types.TracebackType
try:
    raise Exception()
except:
    exc_type
