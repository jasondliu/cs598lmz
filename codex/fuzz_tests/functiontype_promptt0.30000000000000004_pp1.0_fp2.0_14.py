import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)

# Test types.MethodType
class C:
    def m(self):
        pass
assert isinstance(C.m, types.MethodType)
assert not isinstance(C.m, types.BuiltinMethodType)
assert not isinstance(C.m, types.FunctionType)
assert not isinstance(C.m, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
import sys
assert isinstance(sys.exit, types.BuiltinMethodType)
assert not isinstance(sys.exit, types.MethodType)
assert not isinstance(sys.exit, types.FunctionType)
assert not isinstance(sys.exit, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
import builtins
assert isinstance(builtins.len, types.BuiltinFunctionType)
assert
