from types import FunctionType
list(FunctionType(l.__code__, globals(), 'x') for l in range(10))
</code>

