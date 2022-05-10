from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
     for f in (lambda x, y=1, *z, a=2, b=3, **w: x + y + a + b + sum(z) + sum(w.values()),))
</code>

