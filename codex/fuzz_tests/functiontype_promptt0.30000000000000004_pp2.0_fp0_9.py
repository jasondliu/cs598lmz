import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
# Test types.UnboundMethodType
class C:
    def m(self): pass
assert isinstance(C.m, types.UnboundMethodType)
# Test types.MethodType
c = C()
assert isinstance(c.m, types.MethodType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)
# Test types.ModuleType
import sys
assert isinstance(sys, types.ModuleType)
# Test types.TracebackType
try:
    raise Exception()
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)
# Test types.FrameType
def g():
    assert isinstance(sys._getframe(), types.FrameType)
g()
# Test types.CodeType
def h(): pass
assert isinstance(h.__code__, types.Code
