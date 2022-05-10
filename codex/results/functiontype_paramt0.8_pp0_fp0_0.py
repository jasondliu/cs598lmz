from types import FunctionType
list(FunctionType(f.__code__, globals())(x) for x in args)

# [1, 4, 9]
</code>

