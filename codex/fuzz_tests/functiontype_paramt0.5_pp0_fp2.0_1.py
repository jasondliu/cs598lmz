from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
     for f in (lambda: (yield from range(10))).gi_frame.f_back.f_locals.values())
</code>

