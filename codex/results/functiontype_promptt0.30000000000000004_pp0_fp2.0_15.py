import types
# Test types.FunctionType
def f():
    pass
assert type(f) is types.FunctionType
assert type(f) is types.BuiltinFunctionType

# Test types.LambdaType
g = lambda x: x
assert type(g) is types.LambdaType

# Test types.GeneratorType
def h():
    yield 1
assert type(h()) is types.GeneratorType

# Test types.BuiltinMethodType
assert type(list.append) is types.BuiltinMethodType

# Test types.MethodType
class C:
    def f(self):
        pass
assert type(C.f) is types.MethodType
assert type(C().f) is types.MethodType

# Test types.UnboundMethodType
assert type(C.f) is types.UnboundMethodType

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType

# Test types.FrameType
def j():
    assert type(sys
