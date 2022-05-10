from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(10))

# 列表推导式
# 列表推导式是Python中最强大的特性之一，它可以用简洁的代码来创建新的列表

# 列表推导式的基本形式如下：
# [expr for val in collection]
# 这里的collection可以是任何可迭代对象，比如列表、元组、字符串、文件、迭代器或生成器。
# 列表推导式的结果是另一个列表，它包含表
