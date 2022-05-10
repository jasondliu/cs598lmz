import types
# Test types.FunctionType
def f(): pass
assert not isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
assert not isinstance(len, types.BuiltinFunctionType)

# Test types.MethodType
assert not isinstance([].append, types.MethodType)

# Test types.BuiltinMethodType
assert not isinstance([].index, types.BuiltinMethodType)

# Test types.LambdaType
assert not isinstance((lambda: None), types.LambdaType)

# Test types.GeneratorType
assert not isinstance((x for x in range(5)), types.GeneratorType)

# Test types.TracebackType
try:
    1/0
except Exception as e:
    tb = e.__traceback__
    assert not isinstance(tb, types.TracebackType)

# Test types.FrameType
def g():
    return sys._getframe()
assert not isinstance(g(), types.FrameType)

# Test types.CodeType
def h(): pass
assert not isinstance(h.__code
