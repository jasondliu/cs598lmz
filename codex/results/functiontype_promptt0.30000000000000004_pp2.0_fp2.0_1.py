import types
# Test types.FunctionType
def f(): pass
assert type(f) == types.FunctionType

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType

# Test types.LambdaType
assert type(lambda x: x) == types.LambdaType

# Test types.GeneratorType
assert type((lambda: (yield))()) == types.GeneratorType

# Test types.CodeType
assert type(f.__code__) == types.CodeType

# Test types.FrameType
assert type(sys._getframe()) == types.FrameType

# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType

# Test types.ModuleType
assert type(types) == types.ModuleType

# Test types.MethodType
class C:
    def f(self): pass
assert type(C.f) == types.MethodType

# Test types.UnboundMethodType
assert type(C.f
