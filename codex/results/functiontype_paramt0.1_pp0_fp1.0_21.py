from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# 使用lambda函数
# 在Python中，lambda函数可以接收任意多个参数（包括可选参数）并且返回单个表达式的值
# lambda函数的语法只包含一个语句，如下：
# lambda [arg1 [,arg2,.....argn]]:expression
# 如下实例：
sum = lambda arg1, arg2: arg1 + arg2
# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))

# return语句
# return [
