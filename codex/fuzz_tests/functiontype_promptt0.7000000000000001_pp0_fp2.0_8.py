import types
# Test types.FunctionType
def func():
    pass

print(type(func) == types.FunctionType)
# True

# Test types.LambdaType
lambda_func = lambda: None
print(type(lambda_func) == types.LambdaType)
# True

# Test types.GeneratorType
gen = (x * x for x in range(2))
print(type(gen) == types.GeneratorType)
# True

# Test types.ModuleType
import sys
print(type(sys) == types.ModuleType)
# True

# Test types.BuiltinFunctionType
print(type(len) == types.BuiltinFunctionType)
# True

# Test types.BuiltinMethodType
print(type([].append) == types.BuiltinMethodType)
# True

# Test types.MethodType
class A(object):
    def method(self):
        pass

a = A()
print(type(a.method) == types.MethodType)
# True

# Test types.UnboundMethodType
print(type(A.method) == types
