import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
# Test types.BuiltinFunctionType
try:
    import builtins
except ImportError:
    import __builtin__ as builtins
assert isinstance(abs, types.BuiltinFunctionType)
# Test types.LambdaType
assert isinstance(lambda x: x, types.LambdaType)
# Test types.GeneratorType
assert isinstance((x for x in range(10)), types.GeneratorType)
# Test types.GeneratorType
assert isinstance(list, types.BuiltinFunctionType)
# Test types.ModuleType
assert isinstance(types, types.ModuleType)

# Test types.TracebackType
import sys
try:
    raise Exception
except:
    assert isinstance(sys.exc_info()[2], types.TracebackType)

# Test types.FrameType
import sys
def f():
    return sys._getframe()
assert isinstance(f(), types.FrameType)

# Test types.CodeType
assert isinstance(f.__
