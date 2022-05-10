from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda') for x in range(10))

# 列表推导式
# 列表推导式是Python中一种强大的数据处理工具，它可以从任何顺序对象中创建列表。
# 列表推导式的语法形式如下：
# [expr for val in collection if condition]
# 这里expr是一个表达式，它会被应用于从集合中每一个元素上。
# 如果条件存在，它也会被应用于每一个元素，并且
