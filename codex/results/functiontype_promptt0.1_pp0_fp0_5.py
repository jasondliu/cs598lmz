import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.MethodType
class A:
    def f(self):
        pass

assert isinstance(A.f, types.MethodType)

# Test types.UnboundMethodType
assert isinstance(A.f.__func__, types.UnboundMethodType)

# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)

# Test types.GeneratorType
def g():
    yield 1

assert isinstance(g(), types.GeneratorType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)

# Test types.TracebackType
try:
    raise Exception
except:
    assert isinstance(sys.exc_info()[2], types.TracebackType)

# Test types.Frame
