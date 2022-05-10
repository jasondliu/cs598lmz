from types import FunctionType
list(FunctionType(x, globals()).__code__.co_varnames)
</code>

