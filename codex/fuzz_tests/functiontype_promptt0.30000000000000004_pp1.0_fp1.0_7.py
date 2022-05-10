import types
# Test types.FunctionType
def f():
    pass

assert type(f) is types.FunctionType
# Test types.LambdaType
f = lambda: None
assert type(f) is types.LambdaType
# Test types.GeneratorType
f = (x for x in range(5))
assert type(f) is types.GeneratorType
# Test types.CodeType
assert type(f.gi_code) is types.CodeType
# Test types.FrameType
def f():
    return type(sys._getframe())

assert f() is types.FrameType
# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType
# Test types.GetSetDescriptorType
class C(object):
    def getx(self):
        return self.__x
    def setx(self, value):
        self.__x = value
    def delx(self):
        del self.__x
    x = property(getx,
