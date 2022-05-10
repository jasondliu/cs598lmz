import types
# Test types.FunctionType
def f():
    pass
type(f) == types.FunctionType

type(f) == types.BuiltinFunctionType

# Test types.LambdaType
type((lambda x: x)) == types.LambdaType

# Test types.GeneratorType
def g():
    yield 1
type(g) == types.GeneratorType

# Test types.CodeType
type(f.__code__) == types.CodeType

# Test types.FrameType
type(sys._getframe()) == types.FrameType

# Test types.TracebackType
try:
    raise Exception
except:
    type(sys.exc_info()[2]) == types.TracebackType

# Test types.GetSetDescriptorType
class C(object):
    def __init__(self):
        self.__x = None
    def getx(self):
        return self.__x
    def setx(self, value):
        self.__x = value
    def delx(self):
        del self.__x
    x = property(
