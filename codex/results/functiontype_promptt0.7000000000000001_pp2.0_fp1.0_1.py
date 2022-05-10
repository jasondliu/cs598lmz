import types
# Test types.FunctionType
from types import FunctionType

def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda : None, types.FunctionType)

# Test types.LambdaType
from types import LambdaType

assert isinstance(lambda : None, LambdaType)

# Test types.GeneratorType
from types import GeneratorType

def g():
    yield
assert isinstance(g(), GeneratorType)
assert isinstance((x for x in range(3)), GeneratorType)

# Test types.CodeType
from types import CodeType

def h(): pass
assert isinstance(h.__code__, CodeType)
assert isinstance((lambda: None).__code__, CodeType)

# Test types.TracebackType
from types import TracebackType
import sys
assert isinstance(sys.exc_info()[2], TracebackType)

# Test types.FrameType
from types import FrameType

def i():
    try:
        1/0
    except:
        import sys
        return sys.exc_info()[2].t
