from types import FunctionType
list(FunctionType(x, globals(), 'x') for x in [lambda: 1, lambda: 2])
</code>

