from types import FunctionType
list(FunctionType(FunctionType.__doc__, globals(), 'FunctionType')
     for _ in iter(int, 1))
</code>

