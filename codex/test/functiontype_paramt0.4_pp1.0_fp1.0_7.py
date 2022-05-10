from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__,
                  closure=f.__closure__) for f in [lambda a, b: a + b, lambda a, b: a - b])

# [<function <lambda> at 0x7f8b6d7b9488>, <function <lambda> at 0x7f8b6d7b9510>]
