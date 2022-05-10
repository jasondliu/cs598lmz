from types import FunctionType
list(FunctionType(f.__code__, globals(), 'tmp')())

## [2, 3, 4, 5, 6]
</code>

