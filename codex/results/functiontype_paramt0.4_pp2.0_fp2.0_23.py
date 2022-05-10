from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'x') for x in range(5))

# list(FunctionType(lambda x: x, globals(), 'x') for x in range(5))
# [<function <lambda> at 0x7f9a8c7e3f28>,
#  <function <lambda> at 0x7f9a8c7e3f28>,
#  <function <lambda> at 0x7f9a8c7e3f28>,
#  <function <lambda> at 0x7f9a8c7e3f28>,
#  <function <lambda> at 0x7f9a8c7e3f28>]

# list(FunctionType(lambda x: x, globals(), 'x') for x in range(5))
# [<function <lambda> at 0x7f9a8c7e3f28>,
#  <function <lambda> at 0x7f9a8c7e3f28>,
#  <function <lambda> at 0x7f9a8c7e3f28>,

