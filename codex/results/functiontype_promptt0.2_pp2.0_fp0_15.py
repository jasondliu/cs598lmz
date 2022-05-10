import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
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
    1/0
except ZeroDivisionError:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)
# Test types.FrameType
def h():
    assert isinstance(sys._getframe(), types.FrameType)

h()
# Test types.GetSetDescriptorType
class C(object):
    def __init__(self, x):
        self.x = x
    def getx(self):
        return self.x
