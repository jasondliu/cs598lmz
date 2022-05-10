from types import FunctionType
list(FunctionType(f.__code__, globals(), name=f.__name__))

# Output:
# [1, 2, 3]
</code>

