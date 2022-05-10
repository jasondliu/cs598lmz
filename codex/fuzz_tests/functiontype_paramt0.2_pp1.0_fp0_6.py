from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'f') for x in range(10))

# [<function f at 0x7f8d6b1f7d90>, <function f at 0x7f8d6b1f7d90>, <function f at 0x7f8d6b1f7d90>, <function f at 0x7f8d6b1f7d90>, <function f at 0x7f8d6b1f7d90>, <function f at 0x7f8d6b1f7d90>, <function f at 0x7f8d6b1f7d90>, <function f at 0x7f8d6b1f7d90>, <function f at 0x7f8d6b1f7d90>, <function f at 0x7f8d6b1f7d90>]

# The function object is created only once, and the same object is used in the list comprehension.

# The same thing happens with generator expressions.

from types import FunctionType
list(FunctionType(lambda x: x, globals
