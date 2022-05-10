import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)

# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)

# Test types.GeneratorType
assert isinstance((lambda: (yield))(), types.GeneratorType)
assert isinstance((x for x in range(5)), types.GeneratorType)
assert isinstance((x for x in range(5)).__iter__(), types.GeneratorType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
assert isinstance((lambda: None).__code__, types.CodeType)

# Test types.FrameType
def g():
    import inspect
    return inspect.currentframe()
assert isinstance(g(), types.FrameType)

# Test types.TracebackType
def h():
    import sys
    return sys.exc_info()[2]
try:
    raise Exception
except:
    assert isinstance(h(), types.Tr
