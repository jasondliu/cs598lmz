from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(10))

# list(FunctionType(lambda x: x, globals()) for x in range(10))
# [<function <lambda> at 0x7f8d9f1e2d08>,
#  <function <lambda> at 0x7f8d9f1e2d90>,
#  <function <lambda> at 0x7f8d9f1e2e18>,
#  <function <lambda> at 0x7f8d9f1e2ea0>,
#  <function <lambda> at 0x7f8d9f1e2f28>,
#  <function <lambda> at 0x7f8d9f1e2fb0>,
#  <function <lambda> at 0x7f8d9f1e3038>,
#  <function <lambda> at 0x7f8d9f1e30c0>,
#  <function <lambda> at 0x7f8d9f1e3148>,
#  <function <lambda> at 0x7
