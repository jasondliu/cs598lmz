from types import FunctionType
list(FunctionType(f, globals()) for f in [lambda: a])
</code>

