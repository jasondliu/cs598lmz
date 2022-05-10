import types
# Test types.FunctionType
def f(): pass
assert type(f) == types.FunctionType
assert type(f) == types.BuiltinFunctionType

# Test types.LambdaType
g = lambda: None
assert type(g) == types.LambdaType

# Test types.GeneratorType
def h(): yield
assert type(h()) == types.GeneratorType

# Test types.CodeType
assert type(f.__code__) == types.CodeType

# Test types.TracebackType
try:
    1/0
except:
    import sys
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType

# Test types.FrameType
def foo():
    frame = sys._getframe()
    assert type(frame) == types.FrameType
foo()

# Test types.ModuleType
assert type(types) == types.ModuleType

# Test types.BuiltinMethodType
assert type(str.upper) == types.BuiltinMethodType

# Test types.MethodType
class A:
   
