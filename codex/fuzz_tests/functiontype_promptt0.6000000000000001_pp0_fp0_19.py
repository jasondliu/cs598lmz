import types
# Test types.FunctionType

def f(): pass
def g(): pass
class C:
    def m(self): pass

assert type(f) is types.FunctionType
assert type(g) is types.FunctionType
assert type(C.m) is types.MethodType
assert type(C().m) is types.MethodType

# Test types.MethodType

assert type(C.m) is types.MethodType
assert type(C().m) is types.MethodType

# Test types.BuiltinFunctionType

import builtins
assert type(len) is types.BuiltinFunctionType
assert type(min) is types.BuiltinFunctionType
assert type(max) is types.BuiltinFunctionType
assert type(abs) is types.BuiltinFunctionType
assert type(iter) is types.BuiltinFunctionType
assert type(open) is types.BuiltinFunctionType
assert type(any) is types.BuiltinFunctionType
assert type(all) is types.BuiltinFunctionType
assert type(sum) is types.BuiltinFunctionType
assert type(range) is types.BuiltinFunctionType
assert type
