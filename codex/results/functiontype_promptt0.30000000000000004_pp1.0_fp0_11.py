import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert isinstance(f, types.BuiltinMethodType)
assert isinstance(f, types.MethodType)
assert isinstance(f, types.LambdaType)

# Test types.MethodType
class C(object):
    def f(self):
        pass

assert isinstance(C.f, types.MethodType)
assert isinstance(C().f, types.MethodType)

# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)

# Test types.GeneratorType
def g():
    yield

assert isinstance(g(), types.GeneratorType)

# Test types.CodeType
assert isinstance(g.__code__, types.CodeType)

# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    assert isinstance(sys.exc_info()[2], types.TracebackType)


