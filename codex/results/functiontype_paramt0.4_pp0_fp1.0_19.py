from types import FunctionType
list(FunctionType(f.__code__, globals(), name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
     for f in [lambda: None])
</code>

