import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType
# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
# Test types.MethodType
class A:
    def f(self):
        pass
a = A()
assert type(a.f) == types.MethodType
# Test types.LambdaType
l = lambda: None
assert type(l) == types.LambdaType
# Test types.GeneratorType
def g():
    yield
assert type(g()) == types.GeneratorType
# Test types.CodeType
assert type(g.__code__) == types.CodeType
# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType
# Test types.FrameType
def h():
    return sys._getframe()
assert type(h()) == types.FrameType
# Test types.GetSetDescriptorType
class B:
    def __get__
