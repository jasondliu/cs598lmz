import types
# Test types.FunctionType
def func1(): pass
assert isinstance(func1, types.FunctionType)

# Test types.LambdaType
func2 = lambda x: x
assert isinstance(func2, types.LambdaType)

# Test types.GeneratorType
def gen():
    yield 1
assert isinstance(gen(), types.GeneratorType)

# Test types.CodeType
assert isinstance(gen.__code__, types.CodeType)

# Test types.FrameType
def foo():
    bar()
def bar():
    import sys
    return sys._getframe(0)
assert isinstance(bar(), types.FrameType)

# Test types.TracebackType
try:
    1/0
except:
    import sys
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.ModuleType
import types
assert isinstance(types, types.ModuleType)

# Test types.BuiltinFunctionType
import builtins
assert isinstance(abs, types.Builtin
