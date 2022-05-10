from types import FunctionType
list(FunctionType(lambda y, x: y ** x, [], {}).__code__.co_consts).index(2)
</code>

