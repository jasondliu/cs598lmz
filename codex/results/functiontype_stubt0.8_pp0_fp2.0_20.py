from types import FunctionType
a = (x for x in [1])

# 判断是否是generator
print(isinstance(a, GeneratorType))
# True

# 判断是否是generator函数
def foo():
    yield 1

print(isinstance(foo, GeneratorType))
# False

print(isinstance(foo, FunctionType))
# True

# 通过类的__iter__方法判断是否是可迭代的
# 方法一，通过内置的iter函数进行判断
from collections import Iterable
print(isinstance('asd', Iterable))
# True
print(isinstance([], Iterable))
# True
print(isinstance({}, Iterable))
# True
print(isinstance((), Iterable))
# True
print(isinstance(100, Iterable)) # 因为根本不存在next方法，所以不可迭代
print
