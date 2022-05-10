import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType

# Test types.BuiltinFunctionType
assert type(abs) == types.BuiltinFunctionType

# Test types.LambdaType
f = lambda x: x
assert type(f) == types.LambdaType

# Test types.GeneratorType
g = (x for x in range(10))
assert type(g) == types.GeneratorType

# Test types.CoroutineType
async def foo():
    await 1
assert type(foo()) == types.CoroutineType

# Test types.ClassType
class Foo:
    pass
assert type(Foo) == types.ClassType

# Test types.TypeType
assert type(Foo) == types.TypeType

# Test types.TracebackType
def f():
    raise Exception
try:
    f()
except Exception as e:
    tb = e.__traceback__
assert type(tb) == types.TracebackType

# Test types.FrameType
def f():
    pass
assert
