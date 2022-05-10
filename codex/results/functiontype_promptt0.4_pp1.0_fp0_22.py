import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType

# Test types.LambdaType
assert type(lambda x: x) == types.LambdaType

# Test types.GeneratorType
def g():
    yield 1
assert type(g()) == types.GeneratorType

# Test types.CodeType
assert type(f.__code__) == types.CodeType

# Test types.FrameType
def h():
    return h.__code__.co_firstlineno
assert type(h.__code__.co_firstlineno) == types.FrameType

# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    tb = sys.exc_info()[2]
assert type(tb) == types.TracebackType

# Test types.GetSetDescriptorType
class A(object):
    def __get__(self, obj, type=None):
        return 1
