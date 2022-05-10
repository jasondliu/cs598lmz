import types
# Test types.FunctionType
assert isinstance(lambda x: x, types.FunctionType)
assert isinstance(lambda x: x, types.BuiltinFunctionType)
assert isinstance(lambda x: x, types.LambdaType)
# Test types.CodeType
assert not isinstance(lambda x: x, types.CodeType)
# Test types.MethodType
# types.MethodType is not exposed in MicroPython
# See https://github.com/micropython/micropython/issues/1930
#assert isinstance(lambda x: x, types.MethodType)

# Test types.GeneratorType
def gen():
    yield 1

assert isinstance(gen(), types.GeneratorType)

# Test types.TracebackType
# types.TracebackType is not exposed in MicroPython
# See https://github.com/micropython/micropython/issues/1930
#assert isinstance(sys.exc_info()[2], types.TracebackType)

# Test types.FrameType
# types.FrameType is not exposed in MicroPython
# See https://github.com/
