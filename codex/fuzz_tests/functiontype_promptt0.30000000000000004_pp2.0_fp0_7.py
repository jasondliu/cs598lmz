import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)

# Test types.LambdaType
g = lambda: None
assert isinstance(g, types.LambdaType)

# Test types.GeneratorType
def h(): yield
assert isinstance(h(), types.GeneratorType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)

# Test types.MethodType
class A:
    def f(self): pass
assert isinstance(A().f, types.MethodType)

# Test types.UnboundMethodType
assert isinstance(A.f, types.UnboundMethodType)

# Test types.ModuleType
import sys
assert isinstance(sys, types.ModuleType)

# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.Traceback
