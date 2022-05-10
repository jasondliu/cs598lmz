from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__,
                  f.__closure__))
</code>

