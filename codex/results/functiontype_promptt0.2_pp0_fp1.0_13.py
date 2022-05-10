import types
# Test types.FunctionType
def f(): pass
assert type(f) == types.FunctionType
assert type(f) == types.BuiltinFunctionType

# Test types.LambdaType
f = lambda: None
assert type(f) == types.LambdaType

# Test types.GeneratorType
def f(): yield 1
assert type(f()) == types.GeneratorType

# Test types.CodeType
def f(): pass
assert type(f.__code__) == types.CodeType

# Test types.TracebackType
try:
    1/0
except:
    import sys
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType

# Test types.FrameType
def f():
    g()
def g():
    import sys
    return sys._getframe()
assert type(f()) == types.FrameType

# Test types.ModuleType
import sys
assert type(sys) == types.ModuleType

# Test types.BuiltinMethodType
import sys
assert type(sys.exit) == types
