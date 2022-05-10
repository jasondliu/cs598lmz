from types import FunctionType
list(FunctionType(lambda x, y: x + y, globals()) for i in range(10))
# [<function <lambda> at 0x7f0dc6f65f28>, <function <lambda> at 0x7f0dc6f65ea0>, <function <lambda> at 0x7f0dc6f65e18>, <function <lambda> at 0x7f0dc6f65d90>, <function <lambda> at 0x7f0dc6f65d08>, <function <lambda> at 0x7f0dc6f65c80>, <function <lambda> at 0x7f0dc6f65bf8>, <function <lambda> at 0x7f0dc6f65b70>, <function <lambda> at 0x7f0dc6f65ae8>, <function <lambda> at 0x7f0dc6f65a60>]

# The same as above, but using a generator comprehension.
(FunctionType(lambda x, y: x + y, globals()) for i in range(10))
# <generator object <genexpr> at 0x7f
