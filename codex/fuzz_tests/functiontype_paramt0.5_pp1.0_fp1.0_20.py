from types import FunctionType
list(FunctionType(lambda a, b: a + b, {}, None, None, None)(1, 2))

from types import MethodType
list(MethodType(lambda a, b: a + b, 1, int)(2))

from types import ModuleType
list(ModuleType('test', 'test'))

from types import TracebackType
list(TracebackType(None, None, None, None))

from types import FrameType
list(FrameType(None, None, None, None, None, None))

from types import CodeType
list(CodeType(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))

from types import SliceType
list(SliceType(1, 1, 1))

from types import EllipsisType
list(EllipsisType)

from types import BuiltinFunctionType
list(BuiltinFunctionType(lambda a, b: a + b, {}))

from types import BuiltinMethodType
list(BuiltinMethodType(lambda a, b: a + b, None
