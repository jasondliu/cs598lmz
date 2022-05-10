import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType

# Test types.BuiltinFunctionType
assert type(abs) is types.BuiltinFunctionType

# Test types.LambdaType
g = lambda x: x
assert type(g) is types.LambdaType

# Test types.GeneratorType
def h(): yield
assert type(h()) is types.GeneratorType

# Test types.CodeType
assert type(f.__code__) is types.CodeType

# Test types.TypeType
assert type(int) is types.TypeType

# Test types.TracebackType
import sys
try:
    1/0
except:
    e,v,tb = sys.exc_info()
    assert type(tb) is types.TracebackType

# Test types.UnboundMethodType
class C:
    def f(self):
        pass
assert type(C.f) is types.UnboundMethodType

# Test types.InstanceType
c = C()
assert type(c) is types.InstanceType

