from types import FunctionType
list(FunctionType(lambda: 0, globals()) for i in range(3))
</code>

