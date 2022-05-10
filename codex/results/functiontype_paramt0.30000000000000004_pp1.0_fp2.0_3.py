from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# CodeType
from types import CodeType
CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')

# FrameType
from types import FrameType
FrameType(None, {}, '', (), ())

# TracebackType
from types import TracebackType
TracebackType(None, None, None)

# SliceType
from types import SliceType
SliceType(None, None, None)

# EllipsisType
from types import EllipsisType
EllipsisType

# BuiltinFunctionType
from types import BuiltinFunctionType
BuiltinFunctionType(None)

# BuiltinMethodType
from types import BuiltinMethodType
BuiltinMethodType(None, None)

# ModuleType
from types import ModuleType
ModuleType('__main__')

# MethodType
from types import MethodType
MethodType(None, None)

# GeneratorType
from types import GeneratorType
GeneratorType(None, None, None)

# GetSet
