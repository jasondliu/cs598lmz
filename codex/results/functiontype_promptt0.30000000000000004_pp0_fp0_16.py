import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert type(lambda: None) is types.FunctionType

# Test types.LambdaType
assert type(lambda: None) is types.LambdaType

# Test types.GeneratorType
def g():
    yield 1
assert type(g()) is types.GeneratorType

# Test types.CodeType
assert type(f.__code__) is types.CodeType

# Test types.FrameType
assert type(sys._getframe()) is types.FrameType

# Test types.TracebackType
try:
    raise Exception
except:
    assert type(sys.exc_info()[2]) is types.TracebackType

# Test types.GetSetDescriptorType
class C(object):
    def getx(self): return self.__x
    def setx(self, value): self.__x = value
    def delx(self): del self.__x
    x = property(getx, setx, delx, doc="descriptor docstring")
assert type
