from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# CodeType
from types import CodeType
CodeType(0, 0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')

# FrameType
from types import FrameType
FrameType(None, {}, '', ())

# TracebackType
from types import TracebackType
TracebackType(None, None, None)

# SliceType
from types import SliceType
SliceType(1, 2, 3)

# EllipsisType
from types import EllipsisType
EllipsisType()

# BuiltinFunctionType
from types import BuiltinFunctionType
BuiltinFunctionType(lambda x: x)

# BuiltinMethodType
from types import BuiltinMethodType
BuiltinMethodType(lambda x: x, None, None)

# MethodType
from types import MethodType
MethodType(lambda x: x, None)

# ModuleType
from types import ModuleType
ModuleType('foo')

# GetSetDescriptorType
from types import GetSetDesc
