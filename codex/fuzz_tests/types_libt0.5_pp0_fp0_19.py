import types
types.FunctionType

# 判断是否是函数
def fn():
    pass

print(type(fn) == types.FunctionType)

# 判断是否是迭代器
from collections import Iterator
print(isinstance(abs, Iterator))
print(isinstance(iter([]), Iterator))

# 判断是否是生成器
def g():
    for i in range(4):
        yield i

print(isinstance(g(), Iterator))

# 判断是否是可迭代对象
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance(g(), Iterable))
print(isinstance((x for x in range(5)), Iterable))

# 判断是否是字典
print(isinstance({}, Iterable))

# 判断是否是字符串
print(isinstance('abc', Iterable
