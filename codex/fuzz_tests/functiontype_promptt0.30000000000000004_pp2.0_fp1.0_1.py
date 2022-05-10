import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert type(f) is types.BuiltinFunctionType
assert type(f) is types.BuiltinMethodType

# Test types.MethodType
class A:
    def f(self): pass
assert type(A.f) is types.MethodType
assert type(A.f) is types.BuiltinMethodType

# Test types.BuiltinMethodType
assert type(int.__add__) is types.BuiltinMethodType

# Test types.LambdaType
assert type(lambda x: x) is types.LambdaType

# Test types.GeneratorType
assert type(x for x in range(10)) is types.GeneratorType

# Test types.CodeType
assert type(f.__code__) is types.CodeType

# Test types.TracebackType
try:
    1 / 0
except:
    import sys
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType

# Test types.FrameType
