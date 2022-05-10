from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, "test_function", f.__defaults__, f.__closure__))
</code>

