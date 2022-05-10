from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(10))

# list(FunctionType(lambda x: x, globals()) for x in range(10))
# [<function <lambda> at 0x7f1f2c9f9488>, <function <lambda> at 0x7f1f2c9f9510>, <function <lambda> at 0x7f1f2c9f9510>, <function <lambda> at 0x7f1f2c9f9510>, <function <lambda> at 0x7f1f2c9f9510>, <function <lambda> at 0x7f1f2c9f9510>, <function <lambda> at 0x7f1f2c9f9510>, <function <lambda> at 0x7f1f2c9f9510>, <function <lambda> at 0x7f1f2c9f9510>, <function <lambda> at 0x7f1f2c9f9510>]

# list(FunctionType(lambda x: x, globals()) for x in range(10))

