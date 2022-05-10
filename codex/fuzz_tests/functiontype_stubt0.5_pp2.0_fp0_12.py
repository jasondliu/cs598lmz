from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 迭代器
from collections.abc import Iterable, Iterator
print(isinstance([], Iterable))
print(isinstance([], Iterator))
print(isinstance(iter([]), Iterator))

# 可迭代对象
# 实现了__iter__方法的对象
# 实现了__next__方法的对象
# 实现了__getitem__方法的对象
# 实现了__contains__方法的对象
# 实现了__reversed__方法的对象

# 可迭代对象
# 实现了__iter__方法的对象
#
