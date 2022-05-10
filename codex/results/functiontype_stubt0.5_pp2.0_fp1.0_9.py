from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(isinstance(a, FunctionType))

# 迭代器
# 任何可迭代对象都可以通过iter()函数转换成迭代器
# 可以通过next(迭代器)获取迭代器的下一个值
# 迭代器是迭代对象，但是迭代对象不一定是迭代器
# 迭代器中的__iter__()方法返回self
# 迭代器中的__next__()方法返回迭代器的下一个元素，如果没有下一个元素，则
