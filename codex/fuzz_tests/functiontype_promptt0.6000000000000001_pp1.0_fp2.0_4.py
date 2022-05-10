import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
# Test types.BuiltinFunctionType
assert isinstance(sorted, types.BuiltinFunctionType)

# Test types.LambdaType
g = lambda a: a
assert isinstance(g, types.LambdaType)

# Test types.GeneratorType
def g():
    yield 1
h = g()
assert isinstance(h, types.GeneratorType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)

# Test types.FrameType
def h():
    assert isinstance(sys._getframe(), types.FrameType)
h()

# Test types.TracebackType
try:
    raise Exception
except:
    assert isinstance(sys.exc_info()[2], types.TracebackType)

# Test types.GetSetDescriptorType
assert isinstance(int.real, types.GetSetDescriptorType)

# Test types.MemberDescriptorType
assert isinstance(int.__dict__
