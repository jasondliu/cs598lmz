import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert isinstance(int, types.FunctionType)
assert isinstance(object, types.FunctionType)
assert isinstance(object(), types.FunctionType)

# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)

# Test types.GeneratorType
def g(): yield 1
assert isinstance(g(), types.GeneratorType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
assert isinstance(g.__code__, types.CodeType)
assert isinstance(lambda: None, types.CodeType)

# Test types.TracebackType
try:
    1/0
except:
    import sys
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType
assert isinstance(sys._getframe(), types.FrameType)


