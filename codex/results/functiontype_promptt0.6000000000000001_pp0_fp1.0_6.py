import types
# Test types.FunctionType
class A(object):
    def f(self): pass
assert isinstance(A.f, types.FunctionType)
assert not isinstance(A.f, types.MethodType)
# Test types.MethodType
assert isinstance(A().f, types.MethodType)
assert not isinstance(A().f, types.FunctionType)
# Test types.BuiltinFunctionType
import math
assert isinstance(math.sqrt, types.BuiltinFunctionType)
assert not isinstance(math.sqrt, types.FunctionType)
# Test types.BuiltinMethodType
assert isinstance("".upper, types.BuiltinMethodType)
assert not isinstance("".upper, types.MethodType)

print("passed all tests..")
