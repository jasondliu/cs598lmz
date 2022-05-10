from types import FunctionType
list(FunctionType(lambda: None, globals()) for i in range(3))
</code>

