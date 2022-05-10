import types
# Test types.FunctionType
def f(): return 1
assert type(f) == types.FunctionType
# Make sure __doc__ is actually a string
assert type(f.__doc__) == str

# Test types.BuiltinFunctionType
import binascii
assert type(binascii.b2a_uu) == types.BuiltinFunctionType

# Test types.LambdaType
x = lambda: 1
assert type(x) == types.LambdaType

# Test types.GeneratorType
import sys
def g(): yield 1
assert type(g()) == types.GeneratorType

# Test types.TracebackType
try:
    1/0
except ZeroDivisionError:
    tb = sys.exc_info()[2]
assert type(tb) == types.TracebackType

# Test types.CodeType
def h(): pass
assert type(h.__code__) == types.CodeType

# Test types.FrameType
def i():
    x = sys._getframe()
assert type(x) == types.FrameType

# Test types
