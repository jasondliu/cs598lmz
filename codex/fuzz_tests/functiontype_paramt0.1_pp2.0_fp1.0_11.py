from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo') for _ in range(10))
</code>

