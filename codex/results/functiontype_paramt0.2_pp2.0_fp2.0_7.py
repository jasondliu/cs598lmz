from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
     for f in (lambda: None, lambda x: None, lambda x, y: None))
# [<function <lambda> at 0x7f5b5e5d5f28>,
#  <function <lambda> at 0x7f5b5e5d5ea0>,
#  <function <lambda> at 0x7f5b5e5d5e18>]

# The following is a function that takes no arguments and returns None
FunctionType(f.__code__, f.__globals__, name=f.__name__,
             argdefs=f.__defaults__, closure=f.__closure__)()
# None

# The following is a function that takes one argument and returns None
FunctionType(f.__code__, f.__globals__, name=f.__name__,
             argdefs=f.__defaults__, closure
