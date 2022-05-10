from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterator))

# 判断一个对象是否可迭代
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# 判断一个对象是否是Iterator对象
from collections import Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
print(isinstance(iter([]), Iterator))
print(isinstance(
