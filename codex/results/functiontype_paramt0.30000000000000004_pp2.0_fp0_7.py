from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda') for x in range(10))
</code>

