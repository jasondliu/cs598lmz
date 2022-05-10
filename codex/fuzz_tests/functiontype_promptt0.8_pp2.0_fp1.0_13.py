import types
# Test types.FunctionType
def f():
    return 42

assert isinstance(f, types.FunctionType)

# Test types.MethodType
class C(object):
    def __init__(self, v):
        self.v = v

    def get_v(self):
        return self.v

c = C(42)
assert isinstance(C.__init__, types.FunctionType)
assert isinstance(c.__init__, types.MethodType)
assert isinstance(c.get_v, types.MethodType)

# Test types.BuiltinFunctionType
import math
assert isinstance(math.sin, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
#assert isinstance(''.join, types.BuiltinMethodType)

# Test types.UnboundMethodType
assert isinstance(C.get_v, types.UnboundMethodType)

# Test types.TracebackType
def f():
    try:
        return 1 / 0
    except:
        return sys.exc_info()[2]

tb = f()

