from types import FunctionType
a = (x for x in [1])
def b():
    pass
print(isinstance(a, GeneratorType))
print(isinstance(b, FunctionType))
print(isinstance(b, GeneratorType))
print(isinstance(a, FunctionType))

# 迭代器
# 可以被for循环遍历的对象统称为可迭代对象：Iterable。
# 可以使用isinstance()判断一个对象是否是Iterable对象
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# 可以被next()函数调用并不断返回下一个值的对
