from types import FunctionType
a = (x for x in [1])
b = [1]
c = 1
d = "1"
e = {1:1}
f = FunctionType(1,1,1)
print(isinstance(a,GeneratorType))
print(isinstance(b,GeneratorType))
print(isinstance(c,GeneratorType))
print(isinstance(d,GeneratorType))
print(isinstance(e,GeneratorType))
print(isinstance(f,GeneratorType))

# 迭代器
from collections import Iterable
from collections import Iterator
a = (x for x in [1])
b = [1]
c = 1
d = "1"
e = {1:1}
f = FunctionType(1,1,1)
print(isinstance(a,Iterable))
print(isinstance(b,Iterable))
print(isinstance(c,Iterable))
print(isinstance(d,Iterable))
print(isinstance(e,Iterable))
print(isinstance(f,Iterable))

print(isinstance(a,Iterator))

