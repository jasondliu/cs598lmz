import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance([].index, types.BuiltinMethodType)
assert isinstance({}.get, types.BuiltinMethodType)

# Test types.MethodType
class C:
    def f(self): pass
assert isinstance(C.f, types.MethodType)
assert isinstance(C().f, types.MethodType)

# Test types.UnboundMethodType
assert isinstance(C.f, types.UnboundMethodType)
assert isinstance(C().f, types.MethodType)

# Test types.TypeType
assert isinstance(C, types.TypeType)
assert isinstance(type, types.TypeType)
assert isinstance(int, types.TypeType)

# Test types.ClassType
class C:
    def f(self): pass
assert isinstance(C, types.ClassType)

# Test types.InstanceType
class
