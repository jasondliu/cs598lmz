import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType

# Test types.LambdaType
g = lambda: None
assert type(g) is types.LambdaType

# Test types.GeneratorType
def h(): yield None
assert type(h()) is types.GeneratorType

# Test types.BuiltinFunctionType
assert type(abs) is types.BuiltinFunctionType

# Test types.BuiltinMethodType
assert type([].append) is types.BuiltinMethodType

# Test types.MethodType
class A:
    def m(self): pass
assert type(A().m) is types.MethodType

# Test types.UnboundMethodType
assert type(A.m) is types.UnboundMethodType

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType

# Test types.GetSetDescriptorType
class A:
    def fget(self): pass
    def f
