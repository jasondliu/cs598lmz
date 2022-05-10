import types
# Test types.FunctionType
def f():
    pass

assert type(f) == types.FunctionType
assert type(f) == types.BuiltinFunctionType

# Test types.LambdaType
g = lambda: None
assert type(g) == types.LambdaType

# Test types.GeneratorType
def h():
    yield

assert type(h()) == types.GeneratorType

# Test types.MethodType
class A:
    def m(self):
        pass

assert type(A.m) == types.MethodType
assert type(A.m) == types.BuiltinMethodType

# Test types.BuiltinMethodType
assert type(list.append) == types.BuiltinMethodType

# Test types.UnboundMethodType
assert type(A.m) == types.UnboundMethodType

# Test types.ModuleType
import sys
assert type(sys) == types.ModuleType

# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert type(tb
