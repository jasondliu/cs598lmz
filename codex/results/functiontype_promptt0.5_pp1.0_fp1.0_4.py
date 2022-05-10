import types
# Test types.FunctionType
assert(type(lambda x: x) == types.FunctionType)

# Test types.LambdaType
assert(type(lambda x: x) == types.FunctionType)

# Test types.GeneratorType
assert(type(x for x in range(10)) == types.GeneratorType)

# Test types.CodeType
assert(type(lambda x: x).__code__ == types.CodeType)

# Test types.FrameType
def f():
    return types.FrameType
assert(f() == types.FrameType)

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert(type(tb) == types.TracebackType)

# Test types.GetSetDescriptorType
class C(object):
    def getx(self): return self.__x
    def setx(self, value): self.__x = value
    def delx(self): del self.__x
    x = property(getx, setx, delx, doc
