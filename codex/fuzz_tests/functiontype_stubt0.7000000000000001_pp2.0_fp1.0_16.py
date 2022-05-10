from types import FunctionType
a = (x for x in [1])
print(type(a))

print(isinstance(a, GeneratorType))
# <class 'generator'>
# True

# 迭代器，迭代器是可以迭代的对象，可以被next()函数调用并不断返回下一个值, 直到最后抛出StopIteration错误表示无法继续返回下一个值了
# 可以被next()函数调用并不断返回下一个值
# 可以是通过iter()函数获得的迭代器
# 可以表示为一个无限大的数列

import sys


