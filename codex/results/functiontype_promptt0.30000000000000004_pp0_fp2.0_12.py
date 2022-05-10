import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
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
assert isinstance(lambda x: x, types.LambdaType)
# Test types.GeneratorType
assert isinstance((x for x in range(10)), types.GeneratorType)
# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
# Test types.FrameType
def g():
    return types.FrameType(sys._getframe())

assert isinstance(g(), types.FrameType)
# Test types.TracebackType
try:
    raise Exception
except:
    assert isinstance(sys.exc_info()[2],
