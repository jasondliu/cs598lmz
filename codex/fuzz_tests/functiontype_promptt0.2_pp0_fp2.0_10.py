import types
# Test types.FunctionType
def f():
    pass
assert type(f) is types.FunctionType

# Test types.BuiltinFunctionType
assert type(abs) is types.BuiltinFunctionType

# Test types.MethodType
class C:
    def m(self):
        pass
assert type(C.m) is types.MethodType

# Test types.UnboundMethodType
assert type(C.m.__func__) is types.UnboundMethodType

# Test types.LambdaType
assert type(lambda: None) is types.LambdaType

# Test types.GeneratorType
assert type((lambda: (yield))()) is types.GeneratorType

# Test types.CodeType
assert type(f.__code__) is types.CodeType

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType

# Test types.FrameType
assert type(tb.tb_frame) is types.FrameType


