from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
     for f in (lambda: (yield from range(10)), lambda x=5: (yield from range(x))))
# [<function <lambda> at 0x7f8d8f8a9488>, <function <lambda> at 0x7f8d8f8a9400>]
