from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
     for f in [lambda x: x, lambda x, y=1: x+y, lambda x, y, z=1: x+y+z])

# [<function <lambda> at 0x7f5b6c5c0f28>,
#  <function <lambda> at 0x7f5b6c5c0ea0>,
#  <function <lambda> at 0x7f5b6c5c0e18>]

# from types import CodeType
# list(CodeType(f.__code__.co_argcount, f.__code__.co_kwonlyargcount,
#               f.__code__.co_nlocals, f.__code__.co_stacksize,
#               f.__code__.co_flags, f.__code__.co_code, f.__code__.co_consts,
#               f.
