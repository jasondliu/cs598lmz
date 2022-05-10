import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)

# Test types.LambdaType
g = lambda: None
assert isinstance(g, types.LambdaType)

# Test types.GeneratorType
def h(): yield None
assert isinstance(h(), types.GeneratorType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
assert isinstance(g.__code__, types.CodeType)
assert isinstance(h.__code__, types.CodeType)

# Test types.TracebackType
try:
    1/0
except:
    import sys
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType
assert isinstance(sys._getframe(), types.FrameType)

# Test types.BufferType
b = memoryview(b"abc")
assert isinstance(b, types.BufferType)

# Test types.ModuleType
import types
assert isinstance(
