from types import FunctionType
list(FunctionType(f.__code__, globals(), 'my_func'))
</code>

