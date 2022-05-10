from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__iter__()) == a)
print(type(a.__next__))
print(type(a.__next__()) == int)
print(type(a.__next__) == FunctionType)

# 迭代器的特点
# 迭代器的特点是：
# 1. 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
# 2. 可以使用isinstance()判断一个对象是否是Iterator对象：
# 3. 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
