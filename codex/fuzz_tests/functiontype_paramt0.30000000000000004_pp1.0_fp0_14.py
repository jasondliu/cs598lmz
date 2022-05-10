from types import FunctionType
list(FunctionType(list(FunctionType.__dict__.items())))

# code object
from types import CodeType
list(CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b''))

# frame object
from types import FrameType
list(FrameType(None, None, None, None, None, None))

# traceback object
from types import TracebackType
list(TracebackType(None, None, None))

# slice object
from types import SliceType
list(SliceType(None, None, None))

# ellipsis object
from types import EllipsisType
list(EllipsisType)

# builtin function or method
from types import BuiltinFunctionType
list(BuiltinFunctionType(None, None, None))

# builtin method descriptor
from types import BuiltinMethodType
list(BuiltinMethodType(None, None))

# method wrapper
from types import MethodWrapperType
list(MethodWrapperType(None, None))

# wrapper descriptor
from types import WrapperDescriptorType
list
