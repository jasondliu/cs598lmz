from types import FunctionType
list(FunctionType(lambda: 0, globals()))

# 列表推导
# 列表推导式比map，filter函数更快
# 生成器表达式比列表推导式更快，但是不能访问元素的索引
# 列表推导式可以访问元素的索引
# 列表推导式可以用在map，filter，reduce函数中
# map函数返回一个迭代器，列表推导式返回一个列表
# map函数可以用于多个序列
#
