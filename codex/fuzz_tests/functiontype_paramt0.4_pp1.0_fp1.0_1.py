from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(10))

# Output:
# [<function <lambda> at 0x7f4d4b4c4f28>,
#  <function <lambda> at 0x7f4d4b4c4ea0>,
#  <function <lambda> at 0x7f4d4b4c4f80>,
#  <function <lambda> at 0x7f4d4b4c4f18>,
#  <function <lambda> at 0x7f4d4b4c4e18>,
#  <function <lambda> at 0x7f4d4b4c4f50>,
#  <function <lambda> at 0x7f4d4b4c4e40>,
#  <function <lambda> at 0x7f4d4b4c4e60>,
#  <function <lambda> at 0x7f4d4b4c4e80>,
#  <function <lambda> at 0x7f4d4b4c4ea8>]
```


