import types
# Test types.FunctionType
def f():
    pass

print(type(f) == types.FunctionType)

# Test types.LambdaType
g = lambda x: x
print(type(g) == types.LambdaType)

# Test types.GeneratorType
def h():
    yield 1

print(type(h()) == types.GeneratorType)

# Test types.BuiltinFunctionType
print(type(len) == types.BuiltinFunctionType)

# Test types.BuiltinMethodType
print(type([].append) == types.BuiltinMethodType)

# Test types.MethodType
class A(object):
    def f(self):
        pass

print(type(A.f) == types.MethodType)

# Test types.UnboundMethodType
print(type(A.f) == types.MethodType)

# Test types.ModuleType
import sys
print(type(sys) == types.ModuleType)

# Test types.TracebackType
try:
    raise Exception()
except:
    print(type(sys.exc
