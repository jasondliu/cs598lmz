import types
types.MethodType(lambda self, x: x*2, None, Foo)

# TODO:
#from types import FunctionType
#FunctionType(lambda x: x*2, {}, None, None)

# TODO:
#from types import LambdaType
#LambdaType(lambda x: x*2, {}, None)

from types import MemberDescriptorType
MemberDescriptorType(lambda x: x*2)

from types import GetSetDescriptorType
GetSetDescriptorType(lambda x: x*2, lambda x: x*2)

# TODO:
#from types import MethodDescriptorType
#MethodDescriptorType(lambda x: x*2)

from types import ModuleType
ModuleType("Foo")

from types import TracebackType
TracebackType("Foo")

from types import FrameType
FrameType("Foo")

from types import CodeType
CodeType("Foo")

# TODO:
#from types import BufferType
#BufferType("Foo")

from types import NotImple
