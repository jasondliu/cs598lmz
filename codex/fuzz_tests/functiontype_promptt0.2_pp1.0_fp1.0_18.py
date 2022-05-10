import types
# Test types.FunctionType
def f():
    pass

print(type(f) is types.FunctionType)

# Test types.LambdaType
g = lambda: None
print(type(g) is types.LambdaType)

# Test types.GeneratorType
def h():
    yield 1

print(type(h()) is types.GeneratorType)

# Test types.BuiltinFunctionType
print(type(len) is types.BuiltinFunctionType)

# Test types.BuiltinMethodType
print(type([].append) is types.BuiltinMethodType)

# Test types.MethodType
class A:
    def m(self):
        pass

print(type(A.m) is types.MethodType)

# Test types.UnboundMethodType
print(type(A.m) is types.UnboundMethodType)

# Test types.ModuleType
import sys
print(type(sys) is types.ModuleType)

# Test types.TracebackType
try:
    raise Exception
except:
    print(type(sys.exc_info
