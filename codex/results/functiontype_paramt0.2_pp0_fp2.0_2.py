from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
     for f in [lambda x: x + 1, lambda x, y: x + y]])

# doctest: +ELLIPSIS
[<function <lambda> at 0x...>, <function <lambda> at 0x...>]

# doctest: +ELLIPSIS
[<function <lambda> at 0x...>, <function <lambda> at 0x...>]

# doctest: +ELLIPSIS
[<function <lambda> at 0x...>, <function <lambda> at 0x...>]

# doctest: +ELLIPSIS
[<function <lambda> at 0x...>, <function <lambda> at 0x...>]

# doctest: +ELLIPSIS
[<function <lambda> at 0x...>, <function <lambda> at 0x...>]

# doctest: +ELLIPSIS
[<function <lambda> at 0x...>, <function <lambda> at 0
