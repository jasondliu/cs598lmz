from types import FunctionType
a = (x for x in [1])
print(type(a) == types.GeneratorType)
print(type(a) == types.GeneratorType)
print(type(a) == FunctionType)
print(type(a) == types.FunctionType)
print(type(a) == types.BuiltinFunctionType)

from collections import Iterable, Iterator
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance(100, Iterable))

print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance(100, Iterator))

print(isinstance(iter([]), Iterator))

print(isinstance([], (list, Iterator)))


# 可迭代对象iterable
# 可迭代对象不一定是迭代器
# 迭代器iterator: Python的Iterator对象表示的是一个数据流，Iterator对象可
