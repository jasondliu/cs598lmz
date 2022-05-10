from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name='name', argdefs=(),
                  closure=f.__closure__)() for f in [a, b, c])
</code>

