import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType
# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
# Test types.GeneratorType
def g():
    yield 1
assert type(g()) == types.GeneratorType
# Test types.CodeType
assert type(f.__code__) == types.CodeType
# Test types.FrameType
def h():
    assert type(sys._getframe()) == types.FrameType
h()
# Test types.TracebackType
try:
    raise Exception
except:
    assert type(sys.exc_info()[2]) == types.TracebackType
# Test types.ModuleType
assert type(types) == types.ModuleType
# Test types.MethodType
class A:
    def m(self):
        pass
assert type(A.m) == types.MethodType
# Test types.UnboundMethodType
assert type(A.m) == types.MethodType
# Test types.ClassType
assert type(A) == types.ClassType
# Test types
