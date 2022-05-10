from types import FunctionType
a = (x for x in [1])
print(type(a))

# type(1) == int

# 判断是否是某种类型可以用isinstance()函数
# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上

# 能用type()判断的基本类型也可以用isinstance()判断
# 并且还可以判断一个变量是否是某些类型中的一种

# 如果要获得一个对象的所有属性和方法，可以使
