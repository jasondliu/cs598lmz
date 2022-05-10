from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__))

# Output:
# [1, 2, 3, 4, 5]
</code>

