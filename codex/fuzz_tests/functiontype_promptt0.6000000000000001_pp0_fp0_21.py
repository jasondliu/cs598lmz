import types
# Test types.FunctionType
import types
def f(): pass
type(f) == types.FunctionType
# True
# Test types.LambdaType
import types
type(lambda: None) == types.LambdaType
# True
# Test types.GeneratorType
import types
def f():
    yield None
g = f()
type(g) == types.GeneratorType
# True
# Test types.GeneratorType
import types
type((x for x in range(10))) == types.GeneratorType
# True
# Test types.CodeType
import types
def f(): pass
type(f.__code__) == types.CodeType
# True
# Test types.TracebackType
import types
try:
    1/0
except:
    import sys
    tb = sys.exc_info()[2]
    type(tb) == types.TracebackType
# True
# Test types.FrameType
import types
def f(): pass
type(f.__code__.co_frame) == types.FrameType
# True
# Test types.BufferType
import types
