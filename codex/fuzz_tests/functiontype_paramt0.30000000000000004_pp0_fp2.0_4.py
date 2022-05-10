from types import FunctionType
list(FunctionType(x.__code__, globals(), 'foo'))
</code>

