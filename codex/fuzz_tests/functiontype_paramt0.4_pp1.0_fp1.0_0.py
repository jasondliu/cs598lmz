from types import FunctionType
list(FunctionType(f.__code__, globals())(*args))
</code>

