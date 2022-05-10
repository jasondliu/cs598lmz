from types import FunctionType
list(FunctionType(lambda: None, globals()) for i in range(10))

# [<function <lambda> at 0x7f8e0a5d0f28>, <function <lambda> at 0x7f8e0a5d0f28>, <function <lambda> at 0x7f8e0a5d0f28>, <function <lambda> at 0x7f8e0a5d0f28>, <function <lambda> at 0x7f8e0a5d0f28>, <function <lambda> at 0x7f8e0a5d0f28>, <function <lambda> at 0x7f8e0a5d0f28>, <function <lambda> at 0x7f8e0a5d0f28>, <function <lambda> at 0x7f8e0a5d0f28>, <function <lambda> at 0x7f8e0a5d0f28>]

# But the same trick doesn't work with classes:

from types import ClassType
list(ClassType('X', (), {}) for i in range(10
