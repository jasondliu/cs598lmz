import types
# Test types.FunctionType
def f(): pass
def g(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(g, types.FunctionType)
assert f != g

# Test types.BuiltinFunctionType
import math
assert isinstance(math.pow, types.BuiltinFunctionType)
assert isinstance(math.sqrt, types.BuiltinFunctionType)
assert math.pow != math.sqrt

# Test types.BuiltinMethodType
import math
assert isinstance(math.pow.__doc__, types.BuiltinMethodType)
assert isinstance(math.sqrt.__doc__, types.BuiltinMethodType)
assert math.pow.__doc__ != math.sqrt.__doc__

# Test types.MethodType
class C(object):
    def f(self): pass
    def g(self): pass
c = C()
assert isinstance(c.f, types.MethodType)
assert isinstance(c.g, types.MethodType)
assert c.f != c.g

# Test types.UnboundMethodType
class
