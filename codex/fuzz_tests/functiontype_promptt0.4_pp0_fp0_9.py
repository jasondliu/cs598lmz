import types
# Test types.FunctionType
def f():
    pass

assert type(f) == types.FunctionType
# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
# Test types.MethodType
class A:
    def f(self):
        pass

a = A()
assert type(a.f) == types.MethodType
# Test types.UnboundMethodType
assert type(A.f) == types.UnboundMethodType
# Test types.LambdaType
assert type(lambda: None) == types.LambdaType
# Test types.GeneratorType
assert type((x for x in range(10))) == types.GeneratorType
# Test types.TracebackType
try:
    1 / 0
except Exception as e:
    assert type(e.__traceback__) == types.TracebackType
# Test types.FrameType
assert type(f.__code__.co_frame) == types.FrameType
# Test types.CodeType
assert type(f.__code__) == types.CodeType
# Test types.GetSetDescriptor
