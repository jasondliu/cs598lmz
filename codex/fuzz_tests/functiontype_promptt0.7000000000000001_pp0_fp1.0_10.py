import types
# Test types.FunctionType type
def f():
    pass

assert type(f) == types.FunctionType
# Test types.GeneratorType type
def g():
    yield

assert type(g()) == types.GeneratorType
# Test types.BuiltinFunctionType type
assert type(sum) == types.BuiltinFunctionType
# Test types.BuiltinMethodType type
assert type(len) == types.BuiltinMethodType
# Test types.LambdaType type
assert type(lambda x: x) == types.LambdaType

# Test types.ModuleType type
import types
assert type(types) == types.ModuleType
# Test types.TracebackType type
import sys
try:
    raise Exception
except:
    e = sys.exc_info()[2]

assert type(e) == types.TracebackType
# Test types.FrameType type
import sys

def f():
    return sys._getframe()

assert type(f()) == types.FrameType
# Test types.GetSetDescriptorType type
class C(object):
    def getx(self
