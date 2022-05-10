import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
# Test types.LambdaType
g = lambda x: x
assert isinstance(g, types.LambdaType)
# Test types.GeneratorType
def gen():
    yield 1

assert isinstance(gen(), types.GeneratorType)
# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
# Test types.TracebackType
try:
    raise Exception
except:
    assert isinstance(sys.exc_info()[2], types.TracebackType)
# Test types.FrameType
assert isinstance(sys._getframe(), types.FrameType)
# Test types.BuiltinFunctionType
assert isinstance(f.__code__.co_code, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance(f.__code__.co_code.__call__, types.BuiltinMethodType)
# Test types.ModuleType
import types as m
assert isinstance(m, types.ModuleType
