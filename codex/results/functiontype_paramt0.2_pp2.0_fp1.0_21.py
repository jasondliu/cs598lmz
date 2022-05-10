from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda') for x in range(10))

# list(FunctionType(lambda x: x, globals(), 'lambda') for x in range(10))
# [<function <lambda> at 0x7f8e8a1c8598>, <function <lambda> at 0x7f8e8a1c8510>, <function <lambda> at 0x7f8e8a1c85e0>, <function <lambda> at 0x7f8e8a1c8668>, <function <lambda> at 0x7f8e8a1c8730>, <function <lambda> at 0x7f8e8a1c87b8>, <function <lambda> at 0x7f8e8a1c8840>, <function <lambda> at 0x7f8e8a1c88c8>, <function <lambda> at 0x7f8e8a1c8950>, <function <lambda> at 0x7f8e8a1c89d8>]

# list(FunctionType(lambda x: x, glob
