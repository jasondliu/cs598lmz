import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.MethodType)
assert not isinstance(f, types.BuiltinMethodType)
# Test types.BuiltinFunctionType
import time
assert isinstance(time.time, types.BuiltinFunctionType)
assert not isinstance(time.time, types.FunctionType)
assert not isinstance(time.time, types.MethodType)
assert not isinstance(time.time, types.BuiltinMethodType)
# Test types.MethodType
class A:
    def f(self):
        pass

assert isinstance(A.f, types.MethodType)
assert not isinstance(A.f, types.FunctionType)
assert not isinstance(A.f, types.BuiltinFunctionType)
assert not isinstance(A.f, types.BuiltinMethodType)
# Test types.BuiltinMethodType
assert isinstance(A.__init__, types.BuiltinMethodType)
assert not isinstance
