from types import FunctionType
list(FunctionType(a,b,c,d))

# python中的列表：[]，元组：(), 字典：{}， 集合：set()
# 列表推导式：简化了列表生成过程，可以节省空间和时间
# x for x in 可迭代对象， if 条件
# 列表推导式返回一个列表
# 用列表推导式生成1到100的平方数列表
[x ** 2 for x in range(1,101)]

# 用列表推导式生成1到100的偶数的平方数列表
