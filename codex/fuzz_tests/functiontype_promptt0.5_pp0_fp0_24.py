import types
# Test types.FunctionType
def func():
    pass

print(type(func) == types.FunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.BuiltinFunctionType
print(type(len) == types.BuiltinFunctionType)
print(type(iter) == types.BuiltinFunctionType)

# Test types.MethodType
a = 'abc'
print(type(a.replace) == types.MethodType)

# Test types.UnboundMethodType
class A:
    def method(self):
        pass
print(type(A.method) == types.UnboundMethodType)

# Test types.ModuleType
import sys
print(type(sys) == types.ModuleType)

# Test types.ClassType
class A:
    pass
print(type(A) == types.ClassType)

# Test types.TypeType
print(type(A) == types.TypeType)

# Test types.InstanceType
a = A()
