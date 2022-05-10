from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, "ret", None, f.__closure__) for f in funcs)
# [<function ret at 0x10c7ee8c8>, <function ret at 0x10c7ee9d8>]
</code>

