import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)
assert not isinstance(f, types.UnboundMethodType)
# Test types.MethodType
class C:
    def f(self): pass
assert isinstance(C.f, types.MethodType)
assert isinstance(C.f, types.BuiltinMethodType)
assert not isinstance(C.f, types.FunctionType)
assert not isinstance(C.f, types.BuiltinFunctionType)
assert not isinstance(C.f, types.UnboundMethodType)
# Test types.UnboundMethodType
assert isinstance(C.f.__get__(None, C), types.UnboundMethodType)
assert isinstance(C.f.__get__(None, C), types.MethodType)
assert isinstance(C.f.__get__(None, C), types.BuiltinMethodType)
assert not isinstance
