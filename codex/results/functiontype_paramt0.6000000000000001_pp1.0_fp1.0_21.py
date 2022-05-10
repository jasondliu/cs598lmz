from types import FunctionType
list(FunctionType(lambda: 0, {}, 'foo') for i in range(10))
# [<function <lambda> at 0x7f5a6c63d6a8>, <function <lambda> at 0x7f5a6c63d6a8>, <function <lambda> at 0x7f5a6c63d6a8>, <function <lambda> at 0x7f5a6c63d6a8>, <function <lambda> at 0x7f5a6c63d6a8>, <function <lambda> at 0x7f5a6c63d6a8>, <function <lambda> at 0x7f5a6c63d6a8>, <function <lambda> at 0x7f5a6c63d6a8>, <function <lambda> at 0x7f5a6c63d6a8>, <function <lambda> at 0x7f5a6c63d6a8>]

# The same result can be achieved with a list comprehension:
list(FunctionType(lambda: 0, {}, 'foo') for i in range(10))
