from types import FunctionType
list(FunctionType(f.__code__, globals(), "func") for f in [f1, f2, f3])

# [<function f1 at 0x7f8a8b43d6a8>, <function f2 at 0x7f8a8b43d048>, <function f3 at 0x7f8a8b43d0d0>]
</code>

