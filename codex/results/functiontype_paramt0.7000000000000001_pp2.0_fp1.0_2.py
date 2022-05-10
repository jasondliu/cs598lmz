from types import FunctionType
list(FunctionType(f.__code__, globals(), 'func'))
[1, 2]
</code>

