from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['__builtins__', '__name__', '__doc__', '__package__']
</code>

