from types import FunctionType
list(FunctionType(lambda x: x, globals()))

# [<function <lambda> at 0x7f9e9f8c8b70>, <function <lambda> at 0x7f9e9f8c8c80>]

# 使用函数类型创建函数
def add(x, y):
    return x + y

add.__code__ = FunctionType(lambda x, y: x - y, globals())
add(2, 3)

# -1

# 函数类型的属性
# 函数类型的属性主要是用来描述函数的，其中最重要的属性是 __code__，它是一个 code 对象，它描述了函数的执行流程，
#
