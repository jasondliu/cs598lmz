import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
# Test types.LambdaType
assert isinstance((lambda: None), types.LambdaType)
# Test types.GeneratorType
def gen():
    yield 1
assert isinstance(gen(), types.GeneratorType)

def gen2():
    yield from range(3)
assert isinstance(gen2(), types.GeneratorType)

# Test types.CodeType
def f():
    pass
assert isinstance(f.__code__, types.CodeType)

# Test types.FrameType
def f():
    assert isinstance(sys._getframe(), types.FrameType)
f()

# Test types.TracebackType
def f():
    try:
        raise Exception
    except Exception:
        assert isinstance(sys.exc_info()[2], types.TracebackType)
f()

# Test types.ModuleType
import math
assert isinstance(math, types.ModuleType)

# Test types.BuiltinFunctionType
import builtins
assert
