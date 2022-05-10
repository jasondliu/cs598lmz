from types import FunctionType
list(FunctionType(x, globals()).__code__.co_freevars)
['y']
</code>

