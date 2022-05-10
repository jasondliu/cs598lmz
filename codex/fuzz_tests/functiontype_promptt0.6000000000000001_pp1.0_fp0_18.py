import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)

# Test types.MethodType
class x:
    def m(self): pass
assert isinstance(x.m, types.MethodType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert isinstance(x.m, types.BuiltinMethodType)

# Test types.UnboundMethodType
assert isinstance(x.m, types.UnboundMethodType)

# Test types.ModuleType
import sys
assert isinstance(sys, types.ModuleType)

# Test types.TracebackType
try:
    raise Exception
except Exception:
    tb = sys.exc_info()[2]
assert isinstance(tb, types.TracebackType)

# Test types.FrameType
def f():
    return sys._getframe()
assert isinstance(f(), types.FrameType)

# Test types.CodeType
assert isinstance(f.func_code, types.CodeType)

# Test types.TypeType

