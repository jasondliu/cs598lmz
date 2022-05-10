from types import FunctionType
list(FunctionType(lambda x, y: x + y, globals(), 'add')(1, 2))

# TypeError: 'function' object is not iterable
list(FunctionType(lambda x, y: x + y, globals(), 'add'))
</code>

