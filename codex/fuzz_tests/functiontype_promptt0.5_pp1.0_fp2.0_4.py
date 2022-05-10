import types
# Test types.FunctionType and types.MethodType
class A:
    def f(self):
        pass

def g():
    pass

a = A()
print isinstance(A.f, types.MethodType)
print isinstance(a.f, types.MethodType)
print isinstance(g, types.FunctionType)
print isinstance(g, types.MethodType)
print isinstance(A.f, types.FunctionType)
print isinstance(a.f, types.FunctionType)

print isinstance(A.f, types.BuiltinMethodType)
print isinstance(a.f, types.BuiltinMethodType)
print isinstance(g, types.BuiltinFunctionType)
print isinstance(g, types.BuiltinMethodType)
print isinstance(A.f, types.BuiltinFunctionType)
print isinstance(a.f, types.BuiltinFunctionType)

print isinstance(A.f, types.UnboundMethodType)
print isinstance(a.f, types.UnboundMethodType)
print isinstance(g, types.UnboundMethodType)
print
