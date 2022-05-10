from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)

# 判断是否是可迭代对象
from collections import Iterable
print(isinstance(a, Iterable))

# 判断是否是迭代器
from collections import Iterator
print(isinstance(a, Iterator))

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：

print(isinstance(iter([]), Iterator))

# Python的for循环本质上就是通过不断调用next()函数实现的，例如：

