import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
def f():
    pass
assert isinstance(len, types.BuiltinFunctionType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)

# Test types.FrameType
def g():
    assert isinstance(_getframe(0), types.FrameType)
g()

# Test types.TracebackType
def f():
    raise Exception
try:
    f()
except Exception:
    tb = _getframe(0).f_back.f_exc_traceback
    assert isinstance(tb, types.TracebackType)
    assert not isinstance(tb.tb_frame, types.TracebackType)
    assert not isinstance(tb.tb_frame, types.FrameType)

# Test types.GeneratorType
def f():
    yield 1
assert isinstance(f(), types.Gener
