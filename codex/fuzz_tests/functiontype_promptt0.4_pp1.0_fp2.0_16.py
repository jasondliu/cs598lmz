import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
assert not isinstance(len, types.FunctionType)
assert isinstance(len, types.BuiltinFunctionType)

# Test types.MethodType
class C(object):
    def m(self):
        pass
assert isinstance(C.m, types.MethodType)
assert isinstance(C().m, types.MethodType)
assert not isinstance(C.m, types.BuiltinMethodType)

# Test types.BuiltinMethodType
assert isinstance(list.append, types.BuiltinMethodType)
assert isinstance([].append, types.BuiltinMethodType)

# Test types.UnboundMethodType
assert isinstance(list.append, types.UnboundMethodType)
assert not isinstance([].append, types.UnboundMethodType)

# Test types.ModuleType
assert isinstance(types, types.ModuleType)
assert isinstance(types, types.ModuleType)
