from types import FunctionType
a = (x for x in [1])
print(type(a))

# 判断是否可迭代
from collections import Iterable
print(isinstance([], Iterable))

# 判断是否可迭代且迭代器
from collections import Iterator
print(isinstance((x for x in range(10)), Iterator))

# 判断是否可迭代且可以迭代多次
from collections import Iterator
print(isinstance([], Iterator))

# 判断是否是可调用
print(isinstance(lambda x: x, FunctionType))

# 判断是否是可调用
print(isinstance(lambda x: x, FunctionType))

# 判断是否是可调用
print(isinstance(lambda x: x, FunctionType))

# 判断是否是可调用
print(isinstance
