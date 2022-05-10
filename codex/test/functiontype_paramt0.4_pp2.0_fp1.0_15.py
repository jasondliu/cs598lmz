from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
     for f in (lambda x: x, lambda x=1: x, lambda x=1, y=2: x + y,
               lambda x, y=2: x + y, lambda x, y, z=3: x + y + z))
# [<function <lambda> at 0x7f7c6f9f6f28>,
#  <function <lambda> at 0x7f7c6f9f6ea0>,
#  <function <lambda> at 0x7f7c6f9f6f80>,
#  <function <lambda> at 0x7f7c6f9f6e18>,
#  <function <lambda> at 0x7f7c6f9f6e60>]

# But the code objects are not equal:
