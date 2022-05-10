import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert type(f) is types.BuiltinFunctionType

# Test types.MethodType
class C:
    def f(): pass
assert type(C.f) is types.MethodType
assert type(C.f) is types.BuiltinMethodType

# Test types.BuiltinMethodType
assert type(list.append) is types.BuiltinMethodType

# Test types.LambdaType
assert type(lambda: None) is types.LambdaType

# Test types.GeneratorType
assert type((lambda: (yield))()) is types.GeneratorType

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
    frame = sys._getframe()
    assert type(frame) is types.
