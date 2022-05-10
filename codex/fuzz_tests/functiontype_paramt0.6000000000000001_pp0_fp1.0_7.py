from types import FunctionType
list(FunctionType(func.__code__, globals(), "func_name"))
</code>

