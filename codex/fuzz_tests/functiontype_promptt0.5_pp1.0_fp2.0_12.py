import types
# Test types.FunctionType
def f(): pass
def g(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(g, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(g, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
import math
assert isinstance(math.pow, types.BuiltinFunctionType)
assert isinstance(math.pow, types.FunctionType)
assert not isinstance(math.pow, types.MethodType)

# Test types.MethodType
class A(object):
    def f(self): pass
    def g(self): pass

a = A()
assert isinstance(a.f, types.MethodType)
assert isinstance(a.g, types.MethodType)
assert isinstance(a.f, types.FunctionType)
assert isinstance(a.g, types.FunctionType)
assert not isinstance(a.f, types.BuiltinFunctionType)
assert not isinstance(a.g, types.BuiltinFunctionType)

# Test
