import types
# Test types.FunctionType
def func(arg): pass
assert type(func) == types.FunctionType


# Test types.LambdaType
lam = lambda arg: arg
assert type(lam) == types.LambdaType

# Test types.GeneratorType
def gen(arg):
    yield arg
g = gen(1)
assert type(g) == types.GeneratorType

# Test types.CodeType
def f(): pass
assert type(f.__code__) == types.CodeType

# Test types.FrameType
def g():
    return inspect.currentframe()
f = g()
assert type(f) == types.FrameType
assert f.f_code.co_name == "g"
assert f.f_back.f_code.co_name == "f"

# Test types.TracebackType
import sys
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType

# Test types.ModuleType
import math
assert type(math) ==
