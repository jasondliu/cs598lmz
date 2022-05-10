gi = (i for i in ())
# Test gi.gi_code
type({}.get) is types.MethodType
# Test gi.gi_frame

# Test inspect.iscode
def f(): pass
co = f.__code__
type(co) is types.CodeType

# Test inspect.istraceback
tb = None
type(tb) is types.TracebackType

# Test inspect.isframe
def f(): pass
f.__code__
fr = f.__code__.co_firstlineno
type(fr) is types.FrameType

# Test inspect.isabstract
from abc import ABCMeta, abstractmethod
class C(metaclass=ABCMeta):
    @abstractmethod
    def meth(self):
        pass
# Code object inspect should work with and without stubs.
def f(): pass
co = f.__code__

# Test inspect.isgeneratorfunction
gi = (i for i in ())
# Test gi.gi_frame
gi.gi_frame.f_lineno

# Test inspect.isgenerator
gi = (i for i in ())
# Test gi
