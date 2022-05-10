import types
# Test types.FunctionType
class A:
    pass
def f(self, x, y, z):
    return 42
# Test types.LambdaType
g = lambda x, y, z: 42
# Test types.GeneratorType
def h():
    yield 42
# Test types.CodeType
class B:
    pass
def i(self, x, y, z):
    return 42
# Test types.MethodType
def j(self, x, y, z):
    return 42
# Test types.BuiltinFunctionType
# Test types.BuiltinMethodType
# Test types.ModuleType
import sys
# Test types.XRangeType
k = xrange(10)
# Test types.SliceType
l = slice(1, 10, 2)
# Test types.EllipsisType
m = Ellipsis
# Test types.TracebackType
def n():
    return 42
try:
    n()
except:
    tb = sys.exc_info()[2]
# Test types.FrameType
def o():
    return 42
try:
    o()
except
