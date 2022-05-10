import types
# Test types.FunctionType
def func():
    pass
print isinstance(func, types.FunctionType)

# Test types.BuiltinFunctionType
print isinstance(len, types.BuiltinFunctionType)

# Test types.MethodType
class A(object):
    def method(self):
        pass
a = A()
print isinstance(a.method, types.MethodType)

# Test types.LambdaType
lam = lambda x: x
print isinstance(lam, types.LambdaType)

# Test types.GeneratorType
gen = (x for x in range(5))
print isinstance(gen, types.GeneratorType)

# Test types.ModuleType
import sys
print isinstance(sys, types.ModuleType)

# Test types.ClassType
class B:
    pass
print isinstance(B, types.ClassType)

# Test types.InstanceType
b = B()
print isinstance(b, types.InstanceType)

# Test types.UnboundMethodType
print isinstance(A.method, types.UnboundMethodType)

#
