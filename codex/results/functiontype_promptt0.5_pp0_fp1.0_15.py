import types
# Test types.FunctionType

def f():
    pass

def g():
    pass

def h():
    pass

print isinstance(f, types.FunctionType)
print isinstance(g, types.FunctionType)
print isinstance(h, types.FunctionType)
print isinstance(f, types.BuiltinFunctionType)
print isinstance(g, types.BuiltinFunctionType)
print isinstance(h, types.BuiltinFunctionType)

print isinstance(f, types.UnboundMethodType)
print isinstance(g, types.UnboundMethodType)
print isinstance(h, types.UnboundMethodType)
print isinstance(f, types.MethodType)
print isinstance(g, types.MethodType)
print isinstance(h, types.MethodType)
