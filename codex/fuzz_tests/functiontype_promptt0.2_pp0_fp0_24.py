import types
# Test types.FunctionType
def f(): pass
assert type(f) == types.FunctionType

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType

# Test types.MethodType
class A:
    def f(self): pass
assert type(A.f) == types.MethodType

# Test types.UnboundMethodType
assert type(A.f.__get__(None, A)) == types.UnboundMethodType

# Test types.LambdaType
assert type(lambda: None) == types.LambdaType

# Test types.GeneratorType
assert type((lambda: (yield))()) == types.GeneratorType

# Test types.CodeType
assert type(f.__code__) == types.CodeType

# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType

# Test types.FrameType
assert type(tb.tb_frame) == types.
