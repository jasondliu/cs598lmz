from types import FunctionType
list(FunctionType(lambda a, b=1, *c, d, e=2, **f: None).__code__.co_varnames)
Out[1]: ['a', 'b', 'd', 'e', 'c', 'f']
</code>

