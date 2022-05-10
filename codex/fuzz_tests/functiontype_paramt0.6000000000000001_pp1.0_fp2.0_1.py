from types import FunctionType
list(FunctionType(f.__code__, {}, 'f') for f in functions)
</code>

