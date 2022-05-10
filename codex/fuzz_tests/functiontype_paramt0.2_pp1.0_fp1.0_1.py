from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(10))

# 列表推导式
# 列表推导式是Python的一个强大特性，它允许你快速构建一个新的列表，而不需要像使用append()或者extend()那样一个一个元素逐个添加。
# 列表推导式的语法是这样的：
# [表达式 for 变量 in 可迭代对象 if 条件]
# 列表推导式的语法是这样的：
# [表达式 for 变量 in 可迭代
