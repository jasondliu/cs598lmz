from types import FunctionType
list(FunctionType(f.__code__, globals(), "foo"))
# [1, 2, 3]
</code>

