from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(10))

# [<function <lambda> at 0x7f7f8d8b6f28>,
#  <function <lambda> at 0x7f7f8d8b6ea0>,
#  <function <lambda> at 0x7f7f8d8b6f80>,
#  <function <lambda> at 0x7f7f8d8b6f98>,
#  <function <lambda> at 0x7f7f8d8b6fb0>,
#  <function <lambda> at 0x7f7f8d8b6fc8>,
#  <function <lambda> at 0x7f7f8d8b6fe0>,
#  <function <lambda> at 0x7f7f8d8b6ff8>,
#  <function <lambda> at 0x7f7f8d8b7010>,
#  <function <lambda> at 0x7f7f8d8b7028>]

# The lambda function is created by the Function
