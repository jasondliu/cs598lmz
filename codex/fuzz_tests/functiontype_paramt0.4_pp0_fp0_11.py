from types import FunctionType
list(FunctionType(lambda: None, globals()) for _ in range(10))
# [<function <lambda> at 0x7f8d8d8c2e18>, <function <lambda> at 0x7f8d8d8c2ea0>, <function <lambda> at 0x7f8d8d8c2f28>, <function <lambda> at 0x7f8d8d8c2fb0>, <function <lambda> at 0x7f8d8d8c3400>, <function <lambda> at 0x7f8d8d8c3488>, <function <lambda> at 0x7f8d8d8c3510>, <function <lambda> at 0x7f8d8d8c3598>, <function <lambda> at 0x7f8d8d8c3620>, <function <lambda> at 0x7f8d8d8c36a8>]

# 使用lambda表达式来创建匿名函数。
# 关键字lambda
