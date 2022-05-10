import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert isinstance(int, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(f, types.BuiltinFunctionType)
assert isinstance(lambda: None, types.BuiltinFunctionType)
assert isinstance(int, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance(f.__call__, types.BuiltinMethodType)
assert isinstance(lambda: None, types.BuiltinMethodType)
assert isinstance(int, types.BuiltinMethodType)

# Test types.MethodType
class A(object):
    def f(self):
        pass
a = A()
assert isinstance(a.f, types.MethodType)

# Test types.UnboundMethodType
assert isinstance(A.f, types.UnboundMethodType)

# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)

#
