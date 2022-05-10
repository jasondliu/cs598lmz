from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda') for _ in range(10))
</code>

