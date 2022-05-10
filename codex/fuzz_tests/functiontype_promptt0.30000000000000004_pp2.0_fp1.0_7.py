import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.LambdaType
assert isinstance((lambda x: x), types.LambdaType)

# Test types.GeneratorType
assert isinstance((x for x in range(10)), types.GeneratorType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType
assert isinstance(tb.tb_frame, types.FrameType)

# Test types.GetSetDescriptorType
class C(object):
    def getx(self): return self.__x
    def setx(self, value): self.__x = value
    def delx(self): del self
