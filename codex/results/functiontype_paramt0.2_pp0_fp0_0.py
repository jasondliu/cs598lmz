from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(10))

# 使用生成器表达式
# 可以使用生成器表达式来创建新的生成器对象
# 生成器表达式的语法跟列表推导式很像，只不过把方括号换成圆括号
# 列表推导式：[expr for val in collection if condition]
# 生成器表达式：(expr for val in collection if condition)
# 列表推导式会返回一个列表，而生成器表达式会返回
