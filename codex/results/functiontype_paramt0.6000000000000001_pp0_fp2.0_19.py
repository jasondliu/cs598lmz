from types import FunctionType
list(FunctionType(x, globals())() for x in [lambda: x for x in range(10)])
</code>

