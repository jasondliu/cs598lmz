import types
# Test types.FunctionType
def foo():
    pass

print(type(foo) == types.FunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.BuiltinFunctionType
print(type(abs) == types.BuiltinFunctionType)
print(type(int) == types.BuiltinFunctionType)

# Test types.BuiltinMethodType
print(type(str.join) == types.BuiltinMethodType)
print(type([].append) == types.BuiltinMethodType)

# Test types.MethodType
class A:
    def foo(self, x):
        pass

a = A()
print(type(a.foo) == types.MethodType)

# Test types.UnboundMethodType
print(type(A.foo) == types.UnboundMethodType)

# Test types.ModuleType
import sys
print(type(sys) == types.ModuleType)

# Test types.TracebackType
try:
    raise Exception
