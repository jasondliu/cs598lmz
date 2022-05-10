from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'my_func') for x in range(10))
</code>

