from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, None, None, f.__closure__)()
     for f in (lambda: i for i in range(100)))
</code>

