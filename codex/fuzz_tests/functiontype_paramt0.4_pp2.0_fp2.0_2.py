from types import FunctionType
list(FunctionType(lambda x: x + 1, globals(), 'foo')(2))

# TypeError: 'function' object is not iterable
# list(FunctionType(lambda x: x + 1, globals(), 'foo'))
</code>

