from types import FunctionType
a = (x for x in [1])
print type(a)

print type([]) == list
print type({}) == dict
def func():
    pass
print type(func) == FunctionType

# 判断class的类型，使用isinstance()函数。
from collections import Iterator
a = (x for x in [])
print isinstance(a, Iterator)

# 判断是否是可迭代对象，使用iter()函数
from collections import Iterable
print isinstance(a, Iterable)
print isinstance([1], Iterable)
print isinstance({}, Iterable)
print isinstance('abc', Iterable)
from collections import Iterable
print isinstance(1, Iterable)
print isinstance({}, Iterable)

for n in [1, 2, 3, 4, 5]:
    print n
for ch in 'ABC':
    print ch
print '#' * 20
