from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, argdefs=f.__defaults__, closure=f.__closure__))
</code>

