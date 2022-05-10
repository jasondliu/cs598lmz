import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType
assert type(f) == types.BuiltinFunctionType

# Test types.GeneratorType
def g():
    yield 1
assert type(g()) == types.GeneratorType

# Test types.LambdaType
l = lambda: None
assert type(l) == types.LambdaType

# Test types.MethodType
class C:
    def m(self):
        pass
assert type(C.m) == types.MethodType
assert type(C().m) == types.MethodType

# Test types.ModuleType
import sys
assert type(sys) == types.ModuleType

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType

# Test types.UnboundMethodType
assert type(C.m) == types.UnboundMethodType

# Test types.BuiltinMethodType
assert type(list.append) == types.Built
