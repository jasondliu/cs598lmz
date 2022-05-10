import types
# Test types.FunctionType
def func(x):
    return x
assert isinstance(func, types.FunctionType)
# Test types.BuiltinFunctionType
assert isinstance(abs, types.BuiltinFunctionType)
# Test types.LambdaType
assert isinstance(lambda x: x, types.LambdaType)
# Test types.GeneratorType
assert isinstance((x for x in range(10)), types.GeneratorType)
# Test types.CodeType
assert isinstance(func.__code__, types.CodeType)
# Test types.FrameType
assert isinstance(_getframe(), types.FrameType)
# Test types.TracebackType
try:
    raise Exception()
except:
    tb = _getframe(1).f_exc_traceback
assert isinstance(tb, types.TracebackType)
# Test types.GetSetDescriptorType
class C(object):
    def getx(self): return self.__x
    def setx(self, value): self.__x = value
    def delx(self): del self.__x
    x
