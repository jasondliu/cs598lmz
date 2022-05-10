import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
# Test types.BuiltinFunctionType
assert isinstance(abs, types.BuiltinFunctionType)
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
# Test types.CoroutineType
async def c():
    pass

assert isinstance(c(), types.CoroutineType)
# Test types.AsyncGeneratorType
async def ag():
    yield 1

assert isinstance(ag(), types.AsyncGeneratorType)
# Test types.TracebackType
try:
    raise Exception
except:
    assert isinstance(sys.
