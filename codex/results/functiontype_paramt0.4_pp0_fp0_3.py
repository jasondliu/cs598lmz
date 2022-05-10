from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(10))

# Output:
# [<function <lambda> at 0x7f2be7b2d950>,
#  <function <lambda> at 0x7f2be7b2d9d8>,
#  <function <lambda> at 0x7f2be7b2da60>,
#  <function <lambda> at 0x7f2be7b2dae8>,
#  <function <lambda> at 0x7f2be7b2db70>,
#  <function <lambda> at 0x7f2be7b2dbe8>,
#  <function <lambda> at 0x7f2be7b2dc70>,
#  <function <lambda> at 0x7f2be7b2dce8>,
#  <function <lambda> at 0x7f2be7b2dd70>,
#  <function <lambda> at 0x7f2be7b2dde8>]

# The above works because the lambda function is created inside the generator
# expression and
