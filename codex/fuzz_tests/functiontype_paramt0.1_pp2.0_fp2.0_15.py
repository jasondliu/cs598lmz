from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# 使用lambda表达式创建匿名函数
# lambda表达式只能包含一个表达式，不能包含多个语句和返回语句
# lambda表达式的语法只包含一个语句，如下：
# lambda [arg1 [,arg2,.....argn]]:expression
# 如下实例：
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))

# return语句
# return [表
