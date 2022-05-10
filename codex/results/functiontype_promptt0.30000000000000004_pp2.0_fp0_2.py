import types
# Test types.FunctionType
def func(): pass
assert type(func) == types.FunctionType

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType

# Test types.LambdaType
assert type(lambda x: x) == types.LambdaType

# Test types.GeneratorType
assert type((x for x in range(10))) == types.GeneratorType

# Test types.CodeType
assert type(func.__code__) == types.CodeType

# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType

# Test types.FrameType
def outer():
    assert type(sys._getframe()) == types.FrameType
outer()

# Test types.GetSetDescriptorType
class C(object):
    def getx(self): return self.__x
    def setx(self, value): self.__x = value
    def delx(self): del self.__x
