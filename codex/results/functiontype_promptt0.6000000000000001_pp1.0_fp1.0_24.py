import types
# Test types.FunctionType
class A(object):
    def f(self):
        pass
def f():
    pass
print isinstance(f, types.FunctionType)
print isinstance(A.f, types.FunctionType)
print isinstance(A().f, types.FunctionType)
print isinstance(lambda x: x, types.FunctionType)
print isinstance(lambda x: x, types.LambdaType)

# Test types.MethodType
print isinstance(A.f, types.MethodType)
print isinstance(A().f, types.MethodType)

# Test types.UnboundMethodType
print isinstance(A.f, types.UnboundMethodType)
print isinstance(A().f, types.UnboundMethodType)

# Test types.BuiltinFunctionType
print isinstance(f, types.BuiltinFunctionType)
print isinstance(A.f, types.BuiltinFunctionType)
print isinstance(A().f, types.BuiltinFunctionType)
print isinstance(abs, types.BuiltinFunctionType)
print isinstance(A.__init__, types
