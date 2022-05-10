from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo').__code__.co_varnames)

# Output:
['__builtins__', '__name__', '__doc__', '__package__']
</code>

