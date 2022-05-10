from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'f') for x in range(100))
</code>

