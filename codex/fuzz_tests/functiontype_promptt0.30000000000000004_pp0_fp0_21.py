import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType

# Test types.LambdaType
l = lambda: None
assert type(l) == types.LambdaType

# Test types.GeneratorType
def g():
    yield
assert type(g()) == types.GeneratorType

# Test types.MethodType
class A:
    def m(self):
        pass
assert type(A().m) == types.MethodType

# Test types.BuiltinFunctionType
assert type(abs) == types.BuiltinFunctionType

# Test types.BuiltinMethodType
assert type([].append) == types.BuiltinMethodType

# Test types.ModuleType
assert type(types) == types.ModuleType

# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType

# Test types.FrameType
def f():
    return sys._getframe()
assert type(f()) == types.
