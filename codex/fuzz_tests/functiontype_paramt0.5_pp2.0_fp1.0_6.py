from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'myfunc') for i in range(3))
</code>

