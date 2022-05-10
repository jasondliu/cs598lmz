from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
     for f in (lambda: None, lambda x: None, lambda x, y: None,
               lambda x=None: None, lambda x, y=None: None,
               lambda x, y=None, *args: None, lambda x, y=None, *args, **kwargs: None))
# [<function <lambda> at 0x7f7f6e9f6ea0>,
#  <function <lambda> at 0x7f7f6e9f6f28>,
#  <function <lambda> at 0x7f7f6e9f6f80>,
#  <function <lambda> at 0x7f7f6e9f6fc8>,
#  <function <lambda> at 0x7f7f6e9f7048>,
#  <function <lambda> at 0x7f7f6e9f70b0>,
#  <function
