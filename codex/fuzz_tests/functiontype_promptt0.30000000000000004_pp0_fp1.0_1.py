import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)

# Test types.MethodType
class C:
    def f(self): pass
assert not isinstance(C.f, types.FunctionType)
assert not isinstance(C.f, types.BuiltinFunctionType)
assert not isinstance(C.f, types.BuiltinMethodType)
assert isinstance(C.f, types.MethodType)

# Test types.BuiltinMethodType
assert isinstance(C().f, types.FunctionType)
assert not isinstance(C().f, types.BuiltinFunctionType)
assert isinstance(C().f, types.BuiltinMethodType)
assert not isinstance(C().f, types.MethodType)

# Test types.ModuleType
import sys
assert isinstance(sys, types.ModuleType)

# Test types.TracebackType
try:
    raise Exception

