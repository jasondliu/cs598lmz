import types
# Test types.FunctionType
def f(): pass
assert type(f) == types.FunctionType
assert isinstance(f, types.FunctionType)
# Test types.GeneratorType
def g(): yield 42
assert type(g()) == types.GeneratorType
assert isinstance(g(), types.GeneratorType)
# Test types.LambdaType
l = lambda: None
assert type(l) == types.LambdaType
assert isinstance(l, types.LambdaType)
# Test types.MethodType
class C:
    def m(self):
        pass
assert type(C().m) == types.MethodType
assert isinstance(C().m, types.MethodType)
# Test types.ModuleType
import types
assert type(types) == types.ModuleType
assert isinstance(types, types.ModuleType)
# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType
    assert isinstance(tb, types.TracebackType)
