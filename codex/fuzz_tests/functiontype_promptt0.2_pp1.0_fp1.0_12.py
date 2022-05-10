import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert type(f) is types.BuiltinFunctionType

def g():
    def h(): pass
    assert type(h) is types.FunctionType
    assert type(h) is types.BuiltinFunctionType

g()

# Test types.LambdaType
assert type(lambda: None) is types.LambdaType
assert type(lambda: None) is types.BuiltinFunctionType

# Test types.GeneratorType
def f():
    yield 1
assert type(f()) is types.GeneratorType

# Test types.CodeType
def f(): pass
assert type(f.__code__) is types.CodeType

# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType

# Test types.FrameType
def f():
    frame = sys._getframe()
    assert type(frame) is types.FrameType


