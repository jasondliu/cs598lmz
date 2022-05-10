from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# 使用lambda表达式创建匿名函数
# lambda表达式创建的函数，其实是FunctionType类型的对象
# 可以使用isinstance()函数判断
from types import FunctionType
isinstance(lambda x: x, FunctionType)

# 匿名函数的定义
# lambda表达式的语法：lambda 参数列表: 表达式
# lambda表达式的参数列表可以有多个，用逗号分隔
# lambda表达式的参数列表不能有默认值
# lambda表
