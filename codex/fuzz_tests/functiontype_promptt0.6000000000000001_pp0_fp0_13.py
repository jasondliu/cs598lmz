import types
# Test types.FunctionType and types.BuiltinFunctionType by defining a
# function and a built-in function.
def func():
    pass

assert isinstance(func, types.FunctionType)

# Test types.LambdaType by building a lambda function.
lamb = lambda x: x
assert isinstance(lamb, types.LambdaType)

# Test types.GeneratorType by building a generator function.
def gen():
    yield 1
g = gen()
assert isinstance(g, types.GeneratorType)

# Test types.CodeType by building a code object.
c = gen.__code__
assert isinstance(c, types.CodeType)

# Test types.TracebackType by building a traceback object.
try:
    raise Exception
except:
    tb = sys.exc_info()[-1]
assert isinstance(tb, types.TracebackType)

# Test types.FrameType by building a frame object.
f = sys._getframe()
assert isinstance(f, types.FrameType)

# Test types.BufferType by building
