from types import FunctionType
list(FunctionType(lambda x: x, globals()))

# 以下两种方法都是可以的
# def test():
#     pass
# list(test)
# list(test())

# 列表推导式
# 列表推导式创建包含对原始元素做出反应的新列表
# 格式：[expression for item in iterable]
# 列表推导式可以指定if子句，以过滤掉不想要的元素
# 格式：[expression for item in iterable if condition]
# 元组推导式
# 格式：(expression for item in iterable)
# 字典推导式
