import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)

# Test types.LambdaType
l = lambda: None
assert isinstance(l, types.LambdaType)

# Test types.GeneratorType
def g():
    yield None
assert isinstance(g(), types.GeneratorType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)

# Test types.MethodType
class A(object):
    def f(self):
        pass
assert isinstance(A().f, types.MethodType)

# Test types.UnboundMethodType
assert isinstance(A.f, types.UnboundMethodType)

# Test types.ModuleType
assert isinstance(types, types.ModuleType)

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb,
