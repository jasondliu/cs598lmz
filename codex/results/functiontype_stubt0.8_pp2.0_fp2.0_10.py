from types import FunctionType
a = (x for x in [1])
isinstance(a,Iterable)

# 判断一个类型是否可以作为迭代器使用,是否可以使用for...in循环
from collections import Iterable
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(100,Iterable))

# 判断一个类型是否可以作为迭代器使用,是否可以使用for...in循环
from collections import Iterator
print(isinstance((x for x in range(10)),Iterator))
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance('abc',Iterator))

# 可以被next()函数调
