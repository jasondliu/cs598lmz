from types import FunctionType
list(FunctionType(lambda x: x, globals()))

# TypeError: 'function' object is not iterable
</code>

