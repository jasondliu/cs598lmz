from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a,FunctionType))
print(isinstance(a,GeneratorType))
print(isinstance(a,Iterable))
print(isinstance(a,Iterator))
print(isinstance(a,list))

print(isinstance(a,(list,GeneratorType)))
# 如果要判断一个对象是否是Iterable对象呢？可以通过collections模块的Iterable类型判断：
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# 如果要判断一个对象是否是Iterator对象呢？可以
