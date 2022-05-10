from types import FunctionType
list(FunctionType(lambda x: x, {}))

# TypeError: 'function' object is not iterable
</code>

