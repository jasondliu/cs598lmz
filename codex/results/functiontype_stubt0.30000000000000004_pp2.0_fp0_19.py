from types import FunctionType
a = (x for x in [1])
type(a)

# 判断是否是可迭代对象
from collections import Iterable
isinstance([], Iterable)

# 判断是否是迭代器
from collections import Iterator
isinstance(a, Iterator)

# 迭代器可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
# 可以使用isinstance()判断一个对象是否是Iterator对象：

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()
