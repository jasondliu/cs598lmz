import types
# Test types.FunctionType
def foo():
    pass

assert isinstance(foo, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.MethodType
class A(object):
    def foo(self):
        pass

assert isinstance(A.foo, types.MethodType)

# Test types.BuiltinMethodType
assert isinstance(A.__init__, types.BuiltinMethodType)

# Test types.ModuleType
assert isinstance(types, types.ModuleType)

# Test types.TracebackType
try:
    raise Exception()
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType
def bar():
    return sys._getframe()

assert isinstance(bar(), types.FrameType)

# Test types.CodeType
assert isinstance(bar.__code__, types.CodeType)

# Test types.GeneratorType
def gen():
    yield
