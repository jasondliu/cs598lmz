from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'foo'))

# TypeError: 'function' object is not iterable
</code>

