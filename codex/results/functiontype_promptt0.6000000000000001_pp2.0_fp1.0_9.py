import types
# Test types.FunctionType
def f1(): pass
assert type(f1) == types.FunctionType
# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
# Test types.MethodType
class A(object):
    def f(self): pass
a = A()
assert type(a.f) == types.MethodType
# Test types.UnboundMethodType
assert type(A.f) == types.UnboundMethodType
# Test types.LambdaType
assert type(lambda x: x) == types.LambdaType
# Test types.GeneratorType
def f():
    yield 1
assert type(f()) == types.GeneratorType
# Test types.CodeType
assert type(f.__code__) == types.CodeType
# Test types.TracebackType
def f():
    raise ValueError
try:
    f()
except ValueError:
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType
# Test types.FrameType
def f():
    return sys._getframe
