from types import FunctionType
list(FunctionType(lambda: None, globals(), '', None, None).__code__.co_varnames)
</code>

