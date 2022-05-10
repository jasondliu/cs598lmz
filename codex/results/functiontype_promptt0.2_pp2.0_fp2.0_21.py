import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert isinstance(f, types.FunctionType)
assert type(lambda: None) is types.FunctionType
assert isinstance(lambda: None, types.FunctionType)
# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert type(iter) is types.BuiltinFunctionType
assert isinstance(iter, types.BuiltinFunctionType)
# Test types.MethodType
class C(object):
    def m(self): pass
assert type(C.m) is types.MethodType
assert isinstance(C.m, types.MethodType)
assert type(C().m) is types.MethodType
assert isinstance(C().m, types.MethodType)
# Test types.UnboundMethodType
assert type(C.m) is types.UnboundMethodType
assert isinstance(C.m, types.UnboundMethodType)
assert type(C().m) is types.MethodType
assert isinstance(C().m,
