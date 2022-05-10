from types import FunctionType
list(FunctionType(lambda:0, globals()) for _ in range(100000))
</code>

