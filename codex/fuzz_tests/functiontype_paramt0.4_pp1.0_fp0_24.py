from types import FunctionType
list(FunctionType(lambda: 0, globals(), 'f') for i in range(10))
</code>

