import types
# Test types.FunctionType
def func():
    pass

print type(func)
print type(func) == types.FunctionType

# Test types.LambdaType
lambda_func = lambda x: x + 1
print type(lambda_func)
print type(lambda_func) == types.LambdaType

# Test types.CodeType
print type(func.func_code)
print type(func.func_code) == types.CodeType

# Test types.TypeType
print type(type)
print type(type) == types.TypeType

# Test types.UnboundMethodType
class A(object):
    def func(self):
        pass

print type(A.func)
print type(A.func) == types.UnboundMethodType

# Test types.InstanceType
a = A()
print type(a)
print type(a) == types.InstanceType

# Test types.MethodType
print type(a.func)
print type(a.func) == types.MethodType

# Test types.BuiltinFunctionType
print type(abs)
print type
