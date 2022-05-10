from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, 'compose', f.__defaults__, f.__closure__)(*a, **k))

# [Finished in 0.1s]
</code>

