import types
# Test types.FunctionType
def f(): pass
assert type(f) == types.FunctionType

# Test types.LambdaType
g = lambda: None
assert type(g) == types.LambdaType

# Test types.GeneratorType
def h():
    yield 42
assert type(h()) == types.GeneratorType

# Test types.MethodType
class A:
    def f(self): pass
assert type(A().f) == types.MethodType

# Test types.BuiltinFunctionType
assert type(abs) == types.BuiltinFunctionType

# Test types.BuiltinMethodType
assert type([].append) == types.BuiltinMethodType

# Test types.ModuleType
import sys
assert type(sys) == types.ModuleType

# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType

# Test types.FrameType
def foo():
    frame = sys._getframe()
    assert type(frame) ==
