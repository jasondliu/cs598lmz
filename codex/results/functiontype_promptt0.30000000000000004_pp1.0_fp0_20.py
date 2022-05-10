import types
# Test types.FunctionType
def func():
    pass

print(type(func) == types.FunctionType)
print(type(lambda: None) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.BuiltinFunctionType
print(type(len) == types.BuiltinFunctionType)
print(type(iter) == types.BuiltinFunctionType)

# Test types.BuiltinMethodType
print(type([].append) == types.BuiltinMethodType)
print(type({}.get) == types.BuiltinMethodType)

# Test types.MethodType
class A:
    def func(self):
        pass

a = A()
print(type(a.func) == types.MethodType)

# Test types.UnboundMethodType
print(type(A.func) == types.UnboundMethodType)

# Test types.ModuleType
import sys
print(type(sys) == types.ModuleType)

# Test types.TracebackType
try:
    raise Exception()
except:
