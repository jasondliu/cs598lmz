from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'f') for x in range(10))

# [<function <lambda> at 0x7f9d9f0e8ea0>,
#  <function <lambda> at 0x7f9d9f0e8f28>,
#  <function <lambda> at 0x7f9d9f0e8f80>,
#  <function <lambda> at 0x7f9d9f0e8fd8>,
#  <function <lambda> at 0x7f9d9f0e9030>,
#  <function <lambda> at 0x7f9d9f0e9088>,
#  <function <lambda> at 0x7f9d9f0e90e0>,
#  <function <lambda> at 0x7f9d9f0e9138>,
#  <function <lambda> at 0x7f9d9f0e9190>,
#  <function <lambda> at 0x7f9d9f0e91e8>]

# 但是，
