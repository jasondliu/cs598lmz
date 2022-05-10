import types
# Test types.FunctionType
def f(): pass
assert type(f) == types.FunctionType
assert type(lambda: None) == types.FunctionType

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
assert type(dir) == types.BuiltinFunctionType
assert type(int) == types.BuiltinFunctionType
assert type(list) == types.BuiltinFunctionType
assert type(sorted) == types.BuiltinFunctionType
assert type(Exception) == types.BuiltinFunctionType

# Test types.BuiltinMethodType
assert type([].append) == types.BuiltinMethodType
assert type({}.get) == types.BuiltinMethodType
assert type(''.join) == types.BuiltinMethodType

# Test types.MethodType
class C:
    def m(self): pass
assert type(C.m) == types.MethodType
assert type(C().m) == types.MethodType

# Test types.UnboundMethodType
assert type(C.m) == types.UnboundMethodType

# Test types.LambdaType
assert type(
