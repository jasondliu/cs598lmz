import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType

# Test types.LambdaType
g = lambda: None
assert type(g) == types.LambdaType

# Test types.GeneratorType
def h():
    yield None
assert type(h()) == types.GeneratorType

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType

# Test types.BuiltinMethodType
assert type([].append) == types.BuiltinMethodType

# Test types.MethodType
class A(object):
    def __init__(self):
        self.x = 1
    def f(self):
        pass
a = A()
assert type(a.f) == types.MethodType

# Test types.UnboundMethodType
assert type(A.f) == types.UnboundMethodType

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType
