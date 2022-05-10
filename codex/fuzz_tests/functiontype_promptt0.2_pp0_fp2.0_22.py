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
def f():
    frame = sys._getframe()
    assert type(frame) is types.FrameType
f()

# Test types.CodeType
def f(): pass
assert type(f.__code__) is types.CodeType

# Test types.TypeType
assert
