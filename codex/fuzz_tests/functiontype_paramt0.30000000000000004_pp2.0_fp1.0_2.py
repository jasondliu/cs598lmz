from types import FunctionType
list(FunctionType(f.__code__, globals(), 'f')() for _ in range(10))
</code>

