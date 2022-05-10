from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(10))

# Output:
# [<function <lambda> at 0x7f8f8f8f8f8f>,
#  <function <lambda> at 0x7f8f8f8f8f8f>,
#  <function <lambda> at 0x7f8f8f8f8f8f>,
#  <function <lambda> at 0x7f8f8f8f8f8f>,
#  <function <lambda> at 0x7f8f8f8f8f8f>,
#  <function <lambda> at 0x7f8f8f8f8f8f>,
#  <function <lambda> at 0x7f8f8f8f8f8f>,
#  <function <lambda> at 0x7f8f8f8f8f8f>,
#  <function <lambda> at 0x7f8f8f8f8f8f>,
#  <function <lambda> at 0x7f8f8f8f
