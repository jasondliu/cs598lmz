import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType

# Test types.LambdaType
l = lambda: None
assert type(l) is types.LambdaType

# Test types.GeneratorType
def g(): yield
assert type(g()) is types.GeneratorType

# Test types.UnboundMethodType
class C:
    def meth(self): pass
assert type(C.meth) is types.UnboundMethodType

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType

# Test types.BuiltinMethodType
assert type([].append) is types.BuiltinMethodType

# Test types.MethodType
assert type([].append) is types.MethodType

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

