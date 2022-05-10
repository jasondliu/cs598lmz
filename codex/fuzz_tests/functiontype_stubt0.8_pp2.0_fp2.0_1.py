from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
c = {x for x in [1]}
print(type(a))
print(type(b))
print(type(c))

#判断一个对象是否是可迭代对象
from collections import Iterable
print(isinstance('abc',Iterable))

#判断是否是可迭代对象，如果是迭代对象，转化为list
c = [x for x in [1,2,3]] if isinstance([],Iterable) else None
print(c)

#判断是否是可迭代对象，如果是迭代对象，转化为list
c = [x for x in 'abc' if isinstance('abc',Iterable)]
print(c)
