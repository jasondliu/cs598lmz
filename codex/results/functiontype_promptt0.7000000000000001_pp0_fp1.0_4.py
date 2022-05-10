import types
# Test types.FunctionType
assert type(print) == types.BuiltinFunctionType
assert type(lambda x: x) == types.LambdaType

# Test types.TracebackType
try:
    raise Exception
except:
    exc_type, exc_value, exc_tb = sys.exc_info()
    assert type(exc_tb) == types.TracebackType

# Test types.MethodType
l = []
assert type(l.append) == types.BuiltinMethodType

# Test types.FrameType
def f():
    caller_frame = sys._getframe(0)
    assert type(caller_frame) == types.FrameType
f()

# Test types.CodeType
def f(): pass
assert type(f.__code__) == types.CodeType

# Test types.EllipsisType
x = ...
assert type(x) == types.EllipsisType

# Test types.NotImplementedType
x = NotImplemented
assert type(x) == types.NotImplementedType

# Test types.coroutine
async
