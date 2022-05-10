import types
# Test types.FunctionType
import types

def foo(): pass

assert isinstance(foo, types.FunctionType)

# Test types.LambdaType
def curry(x,y,z=None): return lambda n: n+x+y+(z or 0)

c = curry(1,2,3)

assert isinstance(c, types.LambdaType)

# Test types.GeneratorType
def mygenerator():
    yield 1
    yield 2
    yield 3

assert isinstance(mygenerator(), types.GeneratorType)

# Test types.TracebackType
import traceback

def f():
    x = 1
    y = 0
    return x/y

try:
    f()
except Exception, e:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)
    
# Test types.FrameType
assert isinstance(f.func_code.co_consts[-1], types.FrameType)

# Test types.CodeType
assert isinstance(f.
