from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda') for x in range(10))

# list(FunctionType(lambda x: x, globals(), 'lambda') for x in range(10))
# [<function <lambda> at 0x7f8d8c0c8f28>, <function <lambda> at 0x7f8d8c0c8ea0>, <function <lambda> at 0x7f8d8c0c8f80>, <function <lambda> at 0x7f8d8c0c8f98>, <function <lambda> at 0x7f8d8c0c8fb0>, <function <lambda> at 0x7f8d8c0c8fc8>, <function <lambda> at 0x7f8d8c0c8fe0>, <function <lambda> at 0x7f8d8c0c8ff8>, <function <lambda> at 0x7f8d8c0c9020>, <function <lambda> at 0x7f8d8c0c9048>]

# list(FunctionType(lambda x
