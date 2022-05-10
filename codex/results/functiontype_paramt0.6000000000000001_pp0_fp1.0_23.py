from types import FunctionType
list(FunctionType(lambda x, y, z: x + y + z, globals())(1, 2, 3))
from types import LambdaType
list(LambdaType(lambda x, y, z: x + y + z, globals())(1, 2, 3))
#from types import CodeType
#CodeType(3, 0, 1, 0, '|\x00|\x01\x17\x00d\x00S\x00', (), (), (), '', '', 0, b'')
from types import ModuleType
list(ModuleType('m'))
from types import BuiltinFunctionType
list(BuiltinFunctionType(len))
from types import FrameType
list(FrameType(None, None, None, None, None, None))
#from types import TracebackType
#TracebackType(None, None, None)
from types import GetSetDescriptorType
list(GetSetDescriptorType(None, None, None, None))
from types import MemberDescriptorType
list(MemberDescriptorType(None))
from types import WrapperDescriptorType
list
