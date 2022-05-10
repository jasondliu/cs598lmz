import types
# Test types.FunctionType
def foo(): pass

assert isinstance(foo, types.FunctionType)

# Test types.LambdaType
bar = lambda: None

assert isinstance(bar, types.LambdaType)

# Test types.GeneratorType
def gen():
    yield 1

assert isinstance(gen(), types.GeneratorType)

# Test types.CodeType
assert isinstance(foo.__code__, types.CodeType)

# Test types.TracebackType
try:
    raise Exception
except Exception:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    assert isinstance(exc_traceback, types.TracebackType)

# Test types.FrameType
assert isinstance(exc_traceback.tb_frame, types.FrameType)

# Test types.BuiltinFunctionType
assert isinstance(abs, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance(list.append, types.BuiltinMethodType)

# Test types.MethodType
assert isinstance(
