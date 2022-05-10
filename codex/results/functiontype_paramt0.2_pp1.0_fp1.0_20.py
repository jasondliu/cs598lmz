from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(10))

# [<function <lambda> at 0x7f8f9c9b4d08>, <function <lambda> at 0x7f8f9c9b4d90>, <function <lambda> at 0x7f8f9c9b4e18>, <function <lambda> at 0x7f8f9c9b4ea0>, <function <lambda> at 0x7f8f9c9b4f28>, <function <lambda> at 0x7f8f9c9b4fb0>, <function <lambda> at 0x7f8f9c9b5048>, <function <lambda> at 0x7f8f9c9b50d0>, <function <lambda> at 0x7f8f9c9b5158>, <function <lambda> at 0x7f8f9c9b51e0>]

# >>> list(FunctionType(lambda x: x, globals()) for x in range(10))[0](1)
# 1

# >>> list(
