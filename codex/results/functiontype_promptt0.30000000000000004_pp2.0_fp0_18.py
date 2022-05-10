import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType
assert type(f) == types.BuiltinFunctionType
assert type(f) == types.BuiltinMethodType

# Test types.MethodType
class C:
    def f(self):
        pass
assert type(C.f) == types.MethodType
assert type(C.f) == types.BuiltinMethodType

# Test types.BuiltinMethodType
assert type(C.__init__) == types.BuiltinMethodType

# Test types.LambdaType
f = lambda: None
assert type(f) == types.LambdaType

# Test types.GeneratorType
def f():
    yield None
assert type(f()) == types.GeneratorType

# Test types.CodeType
assert type(f.__code__) == types.CodeType

# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType
