import types
# Test types.FunctionType
def f():
    pass

assert type(f) is types.FunctionType
assert type(f) is types.BuiltinFunctionType

# Test types.CodeType
assert type(f.__code__) is types.CodeType

# Test types.GeneratorType
g = (x for x in range(10))
assert type(g) is types.GeneratorType

# Test types.LambdaType
l = lambda x: x
assert type(l) is types.LambdaType

# Test types.ModuleType
import sys
assert type(sys) is types.ModuleType

# Test types.TracebackType
def g():
    return 1/0
try:
    g()
except ZeroDivisionError:
    exc, val, tb = sys.exc_info()
assert type(tb) is types.TracebackType

# Test types.GetSetDescriptorType
class C(object):
    def __init__(self, value):
        self._x = value
    def getx(self):
        return self._x
   
