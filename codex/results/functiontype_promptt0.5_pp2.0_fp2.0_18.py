import types
# Test types.FunctionType
def f(x):
    return x + 1

assert isinstance(f, types.FunctionType)

# Test types.LambdaType
assert isinstance((lambda x: x + 1), types.LambdaType)

# Test types.GeneratorType
assert isinstance((x for x in range(3)), types.GeneratorType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
assert isinstance((lambda x: x + 1).__code__, types.CodeType)
assert isinstance((x for x in range(3)).__code__, types.CodeType)

# Test types.FrameType
def f(x):
    return g(x)

def g(x):
    return sys._getframe()

assert isinstance(f(1), types.FrameType)

# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test
