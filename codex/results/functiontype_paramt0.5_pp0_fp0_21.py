from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f.__defaults__, closure=f.__closure__))

# OUT: [1, 2, 3, 4, 5, 6, 7, 8, 9]
</code>

