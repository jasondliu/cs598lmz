import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)

# Test types.LambdaType
f = lambda: None
assert isinstance(f, types.LambdaType)
assert isinstance(f, types.BuiltinFunctionType)

# Test types.GeneratorType
def f():
    yield None
g = f()
assert isinstance(g, types.GeneratorType)

# Test types.CodeType
def f():
    pass
assert isinstance(f.__code__, types.CodeType)

# Test types.FrameType
def f():
    return f.__code__.__code__.co_filename
assert isinstance(f(), str)

# Test types.TracebackType
try:
    raise Exception
except Exception:
    assert isinstance(sys.exc_info()[2], types.TracebackType)

# Test types.ModuleType
assert isinstance(sys, types.ModuleType)

# Test types.BuiltinMethodType
assert
