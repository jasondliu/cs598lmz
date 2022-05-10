import types
# Test types.FunctionType
def f(): pass
assert type(f) == types.FunctionType

# Test types.LambdaType
x = lambda: None
assert type(x) == types.LambdaType

# Test types.GeneratorType
def g(): yield 42
assert type(g()) == types.GeneratorType

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType

# Test types.BuiltinMethodType
assert type([].append) == types.BuiltinMethodType

# Test types.MethodType
class C:
    def meth(self): pass
assert type(C().meth) == types.MethodType

# Test types.UnboundMethodType
assert type(C.meth) == types.UnboundMethodType

# Test types.ModuleType
import sys
assert type(sys) == types.ModuleType

# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType

