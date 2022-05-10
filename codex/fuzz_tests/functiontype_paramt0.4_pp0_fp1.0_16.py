from types import FunctionType
list(FunctionType(lambda x: x+1, globals(), 'add')(1))

# 使用lambda表达式创建匿名函数
add = lambda x, y: x+y
print(add(1, 2))

# lambda表达式的基本结构
# lambda <参数1>, <参数2>, ……, <参数n>: <表达式>
# lambda表达式的参数必须是单个的，不能定义多个参数，不能使用默认参数、可变参数和关键字参数
# lambda表达式的返回值是单个表达式的计算结果，
