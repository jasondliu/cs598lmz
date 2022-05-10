import types
types.MethodType(a, None, None)

# types.BuiltinFunctionType
import time
time.time

# types.LambdaType
lambda x: x

# types.GeneratorType
(x for x in range(5))

# types.TracebackType
try:
    1/0
except:
    import sys
    sys.exc_info()[2]

# types.CodeType
def f(): pass
f.__code__

# types.FrameType
def f():
    import sys
    return sys._getframe()
f()

# types.EllipsisType
Ellipsis

# types.NotImplementedType
NotImplemented

# types.GetSetDescriptorType
class C(object):
    def getx(self): return self.__x
    def setx(self, value): self.__x = value
    def delx(self): del self.__x
    x = property(getx, setx, delx, doc="I'm the 'x' property.")
C.x.__get
