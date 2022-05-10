import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType

# Test types.MethodType
class C:
    def m(self): pass
assert type(C.m) is types.MethodType

# Test types.UnboundMethodType
assert type(C.m) is types.MethodType
assert type(C.m) is types.UnboundMethodType

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
def g():
    return sys._getframe()
assert type(g()) is types.FrameType

# Test types.CodeType
assert type(g.__code__) is types.CodeType

# Test types.TypeType
assert type(int) is types.TypeType

