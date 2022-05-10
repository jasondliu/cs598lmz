from types import FunctionType
list(FunctionType(lambda: None, globals()) for i in range(10))
</code>

