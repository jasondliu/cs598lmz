from types import FunctionType
list(FunctionType("pass", {}).__globals__)

from types import MemberDescriptorType
list(MemberDescriptorType("pass", {}).__globals__)

from types import MethodType
list(MethodType("pass", {}).__globals__)

from types import ModuleType
list(ModuleType("pass", {}).__globals__)

from types import TracebackType
list(TracebackType("pass").__globals__)

from types import FrameType
list(FrameType("pass").__globals__)

list(object.__globals__)

list(int.__globals__)

list(type.__globals__)

list(str.__globals__)

list(float.__globals__)

list(bytes.__globals__)

list(bool.__globals__)

def f():
    list(list.__globals__)
    x = 0
    list(x.__globals__)

f()

class
