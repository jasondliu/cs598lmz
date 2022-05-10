from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda') for x in range(10))

# list(FunctionType(lambda x: x, globals(), 'lambda') for x in range(10))
# [<function <lambda> at 0x7f6e9d7d8e18>,
#  <function <lambda> at 0x7f6e9d7d8ea0>,
#  <function <lambda> at 0x7f6e9d7d8f28>,
#  <function <lambda> at 0x7f6e9d7d8fb0>,
#  <function <lambda> at 0x7f6e9d7d9090>,
#  <function <lambda> at 0x7f6e9d7d9118>,
#  <function <lambda> at 0x7f6e9d7d91a0>,
#  <function <lambda> at 0x7f6e9d7d9228>,
#  <function <lambda> at 0x7f6e9d7d92b0>,
#  <function <lambda
