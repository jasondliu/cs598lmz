import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType

# Test types.MethodType
class C:
    def meth(self): pass
assert type(C.meth) is types.MethodType
assert type(C().meth) is types.MethodType

# Test types.UnboundMethodType
assert type(C.meth) is types.UnboundMethodType

# Test types.LambdaType
l = lambda: None
assert type(l) is types.LambdaType

# Test types.GeneratorType
def g(): yield 1
assert type(g()) is types.GeneratorType

# Test types.CodeType
assert type(f.__code__) is types.CodeType

# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType

# Test types.FrameType
def f():

