import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
class A:
    def f(): pass
assert type(A.f) is types.FunctionType

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
assert type(A.f) is not types.BuiltinFunctionType

# Test types.MethodType
assert type(A().f) is types.MethodType

# Test types.UnboundMethodType
assert type(A.f) is types.UnboundMethodType

# Test types.ModuleType
import sys
assert type(sys) is types.ModuleType

# Test types.TracebackType
try:
    raise Exception()
except:
    import sys
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType

# Test types.FrameType
def f():
    import sys
    return sys._getframe()
assert type(f()) is types.FrameType

# Test types.CodeType
assert type(f.__code__) is types
