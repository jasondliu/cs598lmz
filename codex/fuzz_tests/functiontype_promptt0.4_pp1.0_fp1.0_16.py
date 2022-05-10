import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert type(f) == types.FunctionType
# Test types.GeneratorType
def f():
    yield 0

assert isinstance(f(), types.GeneratorType)
assert type(f()) == types.GeneratorType
# Test types.LambdaType
l = lambda: None

assert isinstance(l, types.LambdaType)
assert type(l) == types.LambdaType
# Test types.MethodType
class Foo:
    def f(self):
        pass

assert isinstance(Foo().f, types.MethodType)
assert type(Foo().f) == types.MethodType
# Test types.ModuleType
import types

assert isinstance(types, types.ModuleType)
assert type(types) == types.ModuleType
# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]

assert isinstance(tb, types.TracebackType)
assert type(t
