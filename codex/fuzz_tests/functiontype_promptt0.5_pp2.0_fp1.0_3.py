import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert isinstance(int, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance(f.__doc__, types.BuiltinMethodType)
assert isinstance(int.__doc__, types.BuiltinMethodType)
assert isinstance(int.__new__, types.BuiltinMethodType)
# Test types.BuiltinFunctionType
assert isinstance(int.__new__, types.BuiltinFunctionType)
assert isinstance(int.__doc__, types.BuiltinFunctionType)
assert isinstance(f.__doc__, types.BuiltinFunctionType)
# Test types.MethodType
class C:
    def f(self):
        pass
assert isinstance(C.f, types.MethodType)
assert isinstance(C().f, types.MethodType)
# Test types.UnboundMethodType
assert isinstance(C.f, types.UnboundMethodType)
assert not isinstance(C().
