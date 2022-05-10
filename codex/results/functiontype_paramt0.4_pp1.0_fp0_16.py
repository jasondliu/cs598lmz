from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(10))
</code>

