from types import FunctionType
list(FunctionType([], None, None, None, None).__code__.co_freevars)

# Output:
['f', 'x']
</code>

