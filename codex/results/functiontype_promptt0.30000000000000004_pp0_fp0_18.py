import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType

# Test types.LambdaType
assert type(lambda: None) == types.LambdaType

# Test types.GeneratorType
def g():
    yield
assert type(g()) == types.GeneratorType

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType

# Test types.BuiltinMethodType
assert type(list.append) == types.BuiltinMethodType

# Test types.MethodType
class C:
    def m(self):
        pass
assert type(C.m) == types.MethodType

# Test types.UnboundMethodType
assert type(C.m) == types.UnboundMethodType

# Test types.ModuleType
assert type(types) == types.ModuleType

# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
assert type(tb) == types.TracebackType

# Test types.FrameType
