import types
# Test types.FunctionType
def func(): pass
print isinstance(func, types.FunctionType)
print isinstance(lambda: None, types.FunctionType)
print isinstance(map, types.FunctionType)
print isinstance(int, types.FunctionType)
print isinstance(None, types.FunctionType)

# Test types.BuiltinFunctionType
print isinstance(func, types.BuiltinFunctionType)
print isinstance(map, types.BuiltinFunctionType)
print isinstance(int, types.BuiltinFunctionType)
print isinstance(None, types.BuiltinFunctionType)

# Test types.MethodType
class A(object):
    def method(self): pass
a = A()
print isinstance(a.method, types.MethodType)
print isinstance(A.method, types.MethodType)
print isinstance(None, types.MethodType)

# Test types.UnboundMethodType
print isinstance(A.method, types.UnboundMethodType)
print isinstance(a.method, types.UnboundMethodType)
print isinstance(None, types.UnboundMethodType
