from types import FunctionType
list(FunctionType(FunctionType.__code__, globals(), 'empty_function_name')) # []

from types import MethodType
list(MethodType(MethodType.__func__, None, None)) # []

from types import TracebackType
list(TracebackType(None)) # []

from types import FrameType
list(FrameType(None)) # TypeError: argument should be a list of modules to reload, not None

from types import BuiltinFunctionType
list(BuiltinFunctionType(list)) # AttributeError: 'builtin_function_or_method' object has no attribute '__code__'

from types import BuiltinMethodType
list(BuiltinMethodType(list)) # AttributeError: 'builtin_function_or_method' object has no attribute '__code__'

def reload_test():
    list(ReloadTest()) # []

reload_test()

from types import get_closure
list(get_closure(reload_test)) # []

from types import get_function_closure
list(get_function_closure(reload_test)) # []
