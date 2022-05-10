from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
     for f in [f1, f2])

# [functools.partial(<function f1 at 0x7f1d7a7c8d90>, a=1), functools.partial(<function f2 at 0x7f1d7a7c8d08>, b=2)]
</code>

