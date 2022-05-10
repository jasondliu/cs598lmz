from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# Output:
# [<function <lambda> at 0x7f9d8c0a4d08>,
#  <function <lambda> at 0x7f9d8c0a4d90>,
#  <function <lambda> at 0x7f9d8c0a4e18>,
#  <function <lambda> at 0x7f9d8c0a4ea0>,
#  <function <lambda> at 0x7f9d8c0a4f28>,
#  <function <lambda> at 0x7f9d8c0a4fb0>,
#  <function <lambda> at 0x7f9d8c0a5048>,
#  <function <lambda> at 0x7f9d8c0a50d0>,
#  <function <lambda> at 0x7f9d8c0a5158>,
#  <function <lambda> at 0x7f9d8c0a5190>,
#  <function <lambda> at 0x
