from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
     for f in (lambda: (yield from range(10)), lambda x=5: (yield from range(x))))
# [<function __main__.<lambda>()>, <function __main__.<lambda>()>]

# Python 3.5
from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
     for f in (lambda: (yield from range(10)), lambda x=5: (yield from range(x))))
# [<function <lambda> at 0x7f7c8b0f8488>, <function <lambda> at 0x7f7c8b0f8400>]

# Python 3.6
from types import FunctionType
list(FunctionType(f.__code__, f.__
