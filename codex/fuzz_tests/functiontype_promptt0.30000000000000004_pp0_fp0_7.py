import types
# Test types.FunctionType
def function():
    pass
print(type(function))
print(type(function) == types.FunctionType)

# Test types.LambdaType
print(type(lambda x: x) == types.LambdaType)

# Test types.GeneratorType
def generator():
    yield 1
print(type(generator()) == types.GeneratorType)

# Test types.GeneratorType
print(type(x for x in range(3)) == types.GeneratorType)

# Test types.BuiltinFunctionType
print(type(len) == types.BuiltinFunctionType)

# Test types.BuiltinMethodType
print(type([].append) == types.BuiltinMethodType)

# Test types.MethodType
class A(object):
    def method(self):
        pass
a = A()
print(type(a.method) == types.MethodType)

# Test types.UnboundMethodType
print(type(A.method) == types.UnboundMethodType)

# Test types.ModuleType
import sys
print(type(sys
