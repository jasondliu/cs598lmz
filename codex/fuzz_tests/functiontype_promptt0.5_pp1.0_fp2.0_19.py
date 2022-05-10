import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)

# Test types.LambdaType
f = lambda x: x
assert isinstance(f, types.LambdaType)

# Test types.GeneratorType
def g(): yield 1
assert isinstance(g(), types.GeneratorType)

# Test types.CodeType
def h(): pass
assert isinstance(h.__code__, types.CodeType)

# Test types.TracebackType
try:
    1/0
except:
    import sys
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType
def i():
    assert isinstance(sys._getframe(), types.FrameType)
i()

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)

# Test types.ModuleType
import sys
assert isinstance
