from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
     for f in (lambda: (yield i) for i in range(10)))
# [<function <lambda> at 0x7f61a4fb43b0>,
#  <function <lambda> at 0x7f61a4fb4510>,
#  <function <lambda> at 0x7f61a4fb4668>,
#  <function <lambda> at 0x7f61a4fb47c0>,
#  <function <lambda> at 0x7f61a4fb4918>,
#  <function <lambda> at 0x7f61a4fb4a70>,
#  <function <lambda> at 0x7f61a4fb4bc8>,
#  <function <lambda> at 0x7f61a4fb4d20>,
#  <function <lambda> at 0x7f61a4fb4e78>,
#  <function <
