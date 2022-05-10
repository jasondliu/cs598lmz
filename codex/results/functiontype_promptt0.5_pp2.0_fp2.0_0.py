import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType

# Test types.BuiltinFunctionType
def f(): pass
assert type(f) is types.FunctionType

# Test types.LambdaType
l = lambda: None
assert type(l) is types.LambdaType

# Test types.GeneratorType
g = (i for i in range(10))
assert type(g) is types.GeneratorType

# Test types.CodeType
def f(): pass
assert type(f.__code__) is types.CodeType

# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType

# Test types.FrameType
def f():
    assert type(sys._getframe()) is types.FrameType
f()

# Test types.MethodType
class A(object):
    def f(self): pass
assert type(A.f) is types.MethodType

# Test types.Unbound
