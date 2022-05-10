import types
types.FunctionType

# 判断一个对象是否是函数
def fn():
    pass

type(fn) == types.FunctionType

# 判断一个对象是否是lambda函数
type(lambda x: x) == types.LambdaType

# 判断一个对象是否是生成器函数
type((x for x in range(10))) == types.GeneratorType

# 判断一个对象是否是迭代器
from collections import Iterator
isinstance((x for x in range(10)), Iterator)

# 判断一个对象是否是可迭代对象
from collections import Iterable
isinstance([], Iterable)
isinstance({}, Iterable)
isinstance('abc', Iterable)
isinstance((x for x in range(10)), Iterable)

