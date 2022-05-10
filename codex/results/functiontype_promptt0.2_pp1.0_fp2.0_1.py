import types
# Test types.FunctionType
def f():
    pass
assert type(f) is types.FunctionType
# Test types.LambdaType
assert type(lambda: None) is types.LambdaType
# Test types.GeneratorType
def g():
    yield
assert type(g()) is types.GeneratorType
# Test types.CodeType
assert type(f.__code__) is types.CodeType
# Test types.FrameType
def h():
    return h.__code__.co_firstlineno
assert type(h()) is types.FrameType
# Test types.TracebackType
try:
    raise Exception
except:
    assert type(sys.exc_info()[2]) is types.TracebackType
# Test types.GetSetDescriptorType
class C(object):
    def __init__(self, value):
        self._value = value
    def getx(self):
        return self._value
    def setx(self, value):
        self._value = value
    def delx(self):
        del self._value
    x = property(getx
