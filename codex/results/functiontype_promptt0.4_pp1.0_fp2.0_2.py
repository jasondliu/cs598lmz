import types
# Test types.FunctionType
def func(x):
    return x
assert isinstance(func, types.FunctionType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
# Test types.MethodType
class A:
    def method(self):
        pass
assert isinstance(A.method, types.MethodType)
# Test types.BuiltinMethodType
assert isinstance(str.__add__, types.BuiltinMethodType)
# Test types.LambdaType
lambda_ = lambda x: x
assert isinstance(lambda_, types.LambdaType)
# Test types.GeneratorType
def generator():
    yield 42
assert isinstance(generator(), types.GeneratorType)
# Test types.CodeType
assert isinstance(func.__code__, types.CodeType)
# Test types.TracebackType
try:
    1/0
except:
    import sys
    assert isinstance(sys.exc_info()[2], types.TracebackType)
# Test types.FrameType
def frame_test():
    frame_
