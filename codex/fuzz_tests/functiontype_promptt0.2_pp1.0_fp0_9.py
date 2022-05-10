import types
# Test types.FunctionType
def f():
    pass

assert type(f) is types.FunctionType
# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
# Test types.LambdaType
assert type(lambda: None) is types.LambdaType
# Test types.GeneratorType
assert type(x for x in range(10)) is types.GeneratorType
# Test types.CodeType
assert type(f.__code__) is types.CodeType
# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType
# Test types.FrameType
def g():
    return sys._getframe()
assert type(g()) is types.FrameType
# Test types.GetSetDescriptorType
class C(object):
    def getx(self): return self.__x
    def setx(self, value): self.__x = value
    def delx(self): del self.__x
    x =
