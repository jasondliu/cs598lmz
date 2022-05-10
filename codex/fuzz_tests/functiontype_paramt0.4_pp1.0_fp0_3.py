from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda') for x in range(10))

# [<function <lambda> at 0x10f3d1f28>,
#  <function <lambda> at 0x10f3d1f80>,
#  <function <lambda> at 0x10f3d1fd8>,
#  <function <lambda> at 0x10f3d2030>,
#  <function <lambda> at 0x10f3d2088>,
#  <function <lambda> at 0x10f3d20e0>,
#  <function <lambda> at 0x10f3d2138>,
#  <function <lambda> at 0x10f3d2190>,
#  <function <lambda> at 0x10f3d21e8>,
#  <function <lambda> at 0x10f3d2240>]

# The lambda functions are all different, and there is no way to make them the
# same.

# In Python 3.8, the new assignment expression operator := allows you to
# assign a value to a variable as part
