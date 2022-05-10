import types
# Test types.FunctionType
def f():
    pass
assert type(f) is types.FunctionType
# Test types.MethodType
class C:
    def f(self):
        pass
assert type(C.f) is types.MethodType
# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
# Test types.BuiltinMethodType
assert type([].append) is types.BuiltinMethodType
# Test types.ModuleType
import sys
assert type(sys) is types.ModuleType
# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType
# Test types.FrameType
def f():
    return sys._getframe()
assert type(f()) is types.FrameType
# Test types.CodeType
assert type(f.__code__) is types.CodeType
# Test types.TypeType
assert type(int) is types.TypeType
# Test types.UnicodeType
assert type(u"") is types.
