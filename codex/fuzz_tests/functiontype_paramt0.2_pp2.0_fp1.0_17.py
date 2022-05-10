from types import FunctionType
list(FunctionType(lambda: None, globals()) for _ in range(10))
</code>

