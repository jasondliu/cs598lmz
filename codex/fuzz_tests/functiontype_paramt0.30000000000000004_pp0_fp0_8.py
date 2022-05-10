from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# CodeType
from types import CodeType
CodeType(0, 0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')

# FrameType
from types import FrameType
FrameType(None, None, None, None, None, None)

# TracebackType
from types import TracebackType
TracebackType(None, None, None)

# SliceType
from types import SliceType
SliceType(0, 0, 0)

# EllipsisType
from types import EllipsisType
EllipsisType()

# NotImplementedType
from types import NotImplementedType
NotImplementedType()

# GetSetDescriptorType
from types import GetSetDescriptorType
GetSetDescriptorType(None, None, None, None)

# MemberDescriptorType
from types import MemberDescriptorType
MemberDescriptorType(None, None, None)

# BuiltinFunctionType
from types import BuiltinFunctionType
Built
